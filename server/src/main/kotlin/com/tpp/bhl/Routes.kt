package com.tpp.bhl

import io.javalin.Javalin

fun Javalin.apiRoutes() = routes {

    get("/stats/:conveyUUID") { context ->
        val conveyUUID = context.pathParam("conveyUUID")
        val stats = ActionDao.calculateStatsDataFor(conveyUUID)
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