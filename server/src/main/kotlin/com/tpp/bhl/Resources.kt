package com.tpp.bhl

import io.javalin.core.JavalinConfig

object Resources {

    fun addFrontend(config: JavalinConfig) {
        config.addStaticFiles("ui")
    }
}