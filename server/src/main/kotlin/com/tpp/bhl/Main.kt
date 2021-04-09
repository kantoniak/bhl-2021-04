package com.tpp.bhl

import io.javalin.Javalin
import io.javalin.apibuilder.ApiBuilder.*
import java.lang.Integer.max
import java.time.Instant
import java.util.*

data class EnterData(val conveyUUID: UUID, val timestamp: Instant)

data class ExitData(val conveyUUID: UUID, val timestamp: Instant)

data class StatsData(val current: Int, val enters: Int, val exists: Int)

object ActionDao {

    private val enters: MutableList<EnterData> = mutableListOf()

    private val exits: MutableList<ExitData> = mutableListOf()

    fun addEnterData(data: EnterData) {
        enters += data
    }

    fun addExitData(data: ExitData) {
        exits += data
    }

    fun calculateStatsDataFor(conveyUUID: UUID): StatsData {
        val entered = enters.filter { it.conveyUUID == conveyUUID }.size
        val exited = exits.filter { it.conveyUUID == conveyUUID }.size
        return StatsData(max(entered - exited, 0), entered, exited)
    }
}

fun main() {

    val app = Javalin.create().apply {
        exception(Exception::class.java) { e, _ -> e.printStackTrace() }
    }.start("0.0.0.0", getEnvPort())

    app.routes {
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
}

private fun getEnvPort(defaultPort: Int = 8080): Int {
    val herokuPort = System.getenv("PORT")
    return herokuPort?.toInt() ?: defaultPort
}