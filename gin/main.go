// main.go
package main

import "github.com/gin-gonic/gin"

func main() {
    r := gin.Default() // 使用默认中间件（logger和recovery）
    r.GET("/", func(c *gin.Context) {
        c.JSON(200, gin.H{ // 返回一个JSON，状态码是200，gin.H是map[string]interface{}的简写
			"message": "hello",
		})
	})
    r.Run(":8080") // 启动服务，并默认监听8080端口
}

