package com.tpp.bhl

import java.util.*

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
        return StatsData(Integer.max(entered - exited, 0), entered, exited)
    }
}