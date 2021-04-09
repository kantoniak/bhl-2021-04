package com.tpp.bhl

import org.jetbrains.exposed.sql.insert
import org.jetbrains.exposed.sql.select
import java.lang.Long.max

object ActionDao {

    fun addEnterData(data: EnterData) {
        Database.execute {
            EnterEvent.insert {
                it[conveyUUID] = data.conveyUUID
                it[timestamp] = data.timestamp
            }
        }
    }

    fun addExitData(data: ExitData) {
        Database.execute {
            ExitEvent.insert {
                it[conveyUUID] = data.conveyUUID
                it[timestamp] = data.timestamp
            }
        }
    }

    fun calculateStatsDataFor(conveyUUID: String): StatsData {
        return Database.execute {
            val entered = EnterEvent.select { EnterEvent.conveyUUID eq conveyUUID }.count()
            val exited = ExitEvent.select { ExitEvent.conveyUUID eq conveyUUID }.count()
            StatsData(max(entered - exited, 0), entered, exited)
        }
    }
}