package com.tpp.bhl

data class EnterData(val conveyUUID: String, val timestamp: Long)

data class ExitData(val conveyUUID: String, val timestamp: Long)

data class ResetData(val conveyUUID: String, val timestamp: Long)

data class StatsData(val current: Long, val enters: Long, val exits: Long)
