package com.tpp.bhl

import io.javalin.Javalin
import io.javalin.apibuilder.ApiBuilder.*
import java.util.*

fun Javalin.apiRoutes() = this.routes {

    get("/stats/:conveyUUID") { context ->
        val conveyUUID = context.pathParam("conveyUUID")
        val uuid = UUID.fromString(conveyUUID)
        val stats = ActionDao.calculateStatsDataFor(uuid)
        context.json(stats)
    }

    post("/enter") { context ->
        val stringData = context.body<EnterData>()
        ActionDao.addEnterData(stringData)
        context.status(201)
    }

    post("/exit") { context ->
        val stringData = context.body<ExitData>()
        ActionDao.addExitData(stringData)
        context.status(201)
    }
}