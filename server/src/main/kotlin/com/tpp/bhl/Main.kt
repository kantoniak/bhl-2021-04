package com.tpp.bhl

import io.javalin.Javalin

fun main() {
    Javalin.create().apply {
        apiRoutes()
        exception(Exception::class.java) { e, _ -> e.printStackTrace() }
    }.start("0.0.0.0", getEnvPort())
}

private fun getEnvPort(defaultPort: Int = 8080): Int {
    val herokuPort = System.getenv("PORT")
    return herokuPort?.toInt() ?: defaultPort
}