package com.tpp.bhl

data class EnterData(val conveyUUID: String, val timestamp: Long)

data class ExitData(val conveyUUID: String, val timestamp: Long)

data class StatsData(val current: Int, val enters: Int, val exists: Int)
