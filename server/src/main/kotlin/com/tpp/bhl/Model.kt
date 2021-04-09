package com.tpp.bhl

import java.time.Instant
import java.util.*

data class EnterData(val conveyUUID: UUID, val timestamp: Instant)

data class ExitData(val conveyUUID: UUID, val timestamp: Instant)

data class StatsData(val current: Int, val enters: Int, val exists: Int)
