package handlers

import (
	"fmt"
	"net/http"
	"os"
	"web/models"

	"github.com/gin-gonic/gin"
)

func Ping(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"message": "pong",
	})
}

func Welcome(c *gin.Context) {
	c.HTML(200, "welcome.html", gin.H{})
}

func GetFlag(c *gin.Context) {
	c.String(200, os.Getenv("FLAG"))
}

func LoadResources(c *gin.Context) {
	filename := c.Query("filename")
	file, err := os.Open("resources/" + filename)
	if err != nil {
		c.String(http.StatusInternalServerError, fmt.Sprintf("Ошибка при чтении файла: %s", err.Error()))
		return
	}
	stat, err := file.Stat()
	if err != nil {
		c.String(500, "Ошибка при получении информации о файле")
		return
	}
	c.Header("Content-Disposition", "inline; filename="+filename)
	// Отправляем содержимое файла обратно клиенту
	http.ServeContent(c.Writer, c.Request, filename, stat.ModTime(), file)

}

func MapPage(c *gin.Context) {
	var fishki []models.Fishka
	var render_fishki []models.Fishka
	fishki = append(fishki, models.Fishka{Decript: "Позиция \"Трусы\"", PATH: "Инферно2.mp4", Map: "Inferno"})
	fishki = append(fishki, models.Fishka{Decript: "Подсадка на козырек (Ветка)", PATH: "Инферно1 (ред).mp4", Map: "Inferno"})
	fishki = append(fishki, models.Fishka{Decript: "Занятие Банана", PATH: "Инферно3.mp4", Map: "Inferno"})
	fishki = append(fishki, models.Fishka{Decript: "Буст тень", PATH: "Мираж1.mp4", Map: "Mirage"})
	fishki = append(fishki, models.Fishka{Decript: "Смок окно с т", PATH: "Мираж2.mp4", Map: "Mirage"})
	fishki = append(fishki, models.Fishka{Decript: "Нычка на А пленту", PATH: "Мираж3.mp4", Map: "Mirage"})
	fishki = append(fishki, models.Fishka{Decript: "Подсадка с А плента", PATH: "Оверпасс1.mp4", Map: "Overpass"})
	fishki = append(fishki, models.Fishka{Decript: "Молик на А плент с Б", PATH: "Оверпасс2.mp4", Map: "Overpass"})
	fishki = append(fishki, models.Fishka{Decript: "Смок на монстр с КТ", PATH: "Оверпасс3.mp4", Map: "Overpass"})
	fishki = append(fishki, models.Fishka{Decript: "Приемка А", PATH: "Эншнт1.mp4", Map: "Ancient"})
	fishki = append(fishki, models.Fishka{Decript: "Смок мид с Т", PATH: "Эншнт2.mp4", Map: "Ancient"})
	fishki = append(fishki, models.Fishka{Decript: "Подсадка на миду", PATH: "Вертиго1.mp4", Map: "Vertigo"})
	fishki = append(fishki, models.Fishka{Decript: "Подсадка на А пленту", PATH: "Вертиго2.mp4", Map: "Vertigo"})

	name_map := c.Param("name_map")
	for _, fishka := range fishki {
		if fishka.Map == name_map {
			render_fishki = append(render_fishki, fishka)
		}
	}

	c.HTML(200, "map.html", gin.H{"fishki": render_fishki, "map": name_map})
}
