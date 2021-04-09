package com.tpp.bhl

import org.jetbrains.exposed.sql.SortOrder
import org.jetbrains.exposed.sql.and
import org.jetbrains.exposed.sql.insert
import org.jetbrains.exposed.sql.select
import java.lang.Long.max

object ActionDao {

    fun addEnterData(data: EnterData) = Database.execute {
        EnterEvent.insert {
            it[conveyUUID] = data.conveyUUID
            it[timestamp] = data.timestamp
        }
    }

    fun addExitData(data: ExitData) = Database.execute {
        ExitEvent.insert {
            it[conveyUUID] = data.conveyUUID
            it[timestamp] = data.timestamp
        }
    }

    fun addResetData(data: ResetData) = Database.execute {
        ResetEvent.insert {
            it[conveyUUID] = data.conveyUUID
            it[timestamp] = data.timestamp
        }
    }

    fun calculateStatsDataFor(conveyUUID: String): StatsData {
        return Database.evaluate {
            val resetTimestamp = ResetEvent
                .select { ResetEvent.conveyUUID eq conveyUUID }
                .orderBy(ResetEvent.timestamp, SortOrder.DESC)
                .firstOrNull()?.get(ResetEvent.timestamp) ?: Long.MIN_VALUE

            val entered = EnterEvent.select {
                (EnterEvent.conveyUUID eq conveyUUID) and (EnterEvent.timestamp greater resetTimestamp)
            }.count()
            val exited = ExitEvent.select {
                (ExitEvent.conveyUUID eq conveyUUID) and (ExitEvent.timestamp greater resetTimestamp)
            }.count()

            StatsData(max(entered - exited, 0), entered, exited)
        }
    }
}