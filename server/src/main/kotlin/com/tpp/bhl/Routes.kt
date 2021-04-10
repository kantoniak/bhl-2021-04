package com.tpp.bhl

import io.javalin.Javalin

private const val CREATED_CODE = 201

fun Javalin.apiRoutes() = routes {

    get("/stats/:conveyUUID") { context ->
        val conveyUUID = context.pathParam("conveyUUID")
        val stats = ActionDao.calculateStatsDataFor(conveyUUID)
        context.header("Access-Control-Allow-Origin", "*")
        context.json(stats)
    }

    post("/enter") { context ->
        val enterData = context.body<EnterData>()
        ActionDao.addEnterData(enterData)
        context.status(CREATED_CODE)
    }

    post("/exit") { context ->
        val exitData = context.body<ExitData>()
        ActionDao.addExitData(exitData)
        context.status(CREATED_CODE)
    }

    post("/reset") { context ->
        val resetData = context.body<ResetData>()
        ActionDao.addResetData(resetData)
        context.status(CREATED_CODE)
    }
}