package com.tpp.bhl

import io.javalin.Javalin

fun main() {
    Database.initTables()

    Javalin.create()
        .apply { exception(Exception::class.java) { e, _ -> e.printStackTrace() } }
        .start("0.0.0.0", Env.getServerPort())
        .apiRoutes()
}



