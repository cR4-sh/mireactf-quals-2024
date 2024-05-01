package main

import (
	"web/handlers"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()
	router.LoadHTMLGlob("templates/*.html")
	router.GET("/", handlers.Welcome)
	router.GET("/:name_map", handlers.MapPage)
	router.GET("/ping", handlers.Ping)
	router.GET("/resources", handlers.LoadResources)
	router.GET("/GetSuperPuperFishku1337", handlers.GetFlag)
	router.Run() // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
