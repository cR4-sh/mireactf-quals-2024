package handlers

import (
	"encoding/base64"
	"encoding/json"
	"log"
	"net/http"
	"os"
	"strings"
	"web/database"

	"github.com/gin-gonic/gin"
)

func Validate(c *gin.Context) {
	// host := c.Request.Host
	data := map[string]interface{}{
		"access": false,
	}
	c.JSON(200, data)
}

func access_verification(c *gin.Context, object database.SCP) bool {
	result := map[string]interface{}{"access": false}
	response, err := http.Get("http://" + c.Request.Host + "/validate")
	if err != nil {
		return false
	}
	defer response.Body.Close()
	json.NewDecoder(response.Body).Decode(&result)
	if access, ok := result["access"].(bool); ok {
		return access
	} else {
		return false
	}
}

func GetMainPage(c *gin.Context) {
	objects := database.GetAll()
	c.HTML(200, "main_page.html", gin.H{"objects": objects})
}

func GetObject(c *gin.Context) {
	object := database.GetByName(c.Param("object"))
	if object.IsSecret {
		if !access_verification(c, object) {
			c.String(200, "Access denied!!!")
			return
		}
	}
	if object == (database.SCP{}) {
		c.String(http.StatusNotFound, "Object not found")
		return
	}
	imageData, err := os.ReadFile("./secret-data/images/" + object.ImagePath)
	if err != nil {
		log.Print(err.Error())
		c.String(http.StatusInternalServerError, "Error reading image")
		return
	}

	description, err := os.ReadFile("./secret-data/description/" + object.DescryptionPath)
	if err != nil {
		log.Print(err.Error())
		c.String(http.StatusInternalServerError, "Error reading descrptoin")
		return
	}
	log.Print(string(description))
	encodedImage := base64.StdEncoding.EncodeToString(imageData)
	c.HTML(200, "object.html", gin.H{"name": object.Name, "imagedata": encodedImage, "description": strings.Split(string(description), "\n")})
}
