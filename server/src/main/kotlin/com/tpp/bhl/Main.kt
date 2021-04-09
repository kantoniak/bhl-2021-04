package com.tpp.bhl

import io.javalin.Javalin
import io.javalin.apibuilder.ApiBuilder.*
import java.util.*

fun main() {
    Javalin.create()
        .apply {
            exception(Exception::class.java) { e, _ -> e.printStackTrace() } }
        .start("0.0.0.0", getEnvPort())
        .apiRoutes()
}

private fun getEnvPort(defaultPort: Int = 8080): Int {
    val herokuPort = System.getenv("PORT")
    return herokuPort?.toInt() ?: defaultPort
}