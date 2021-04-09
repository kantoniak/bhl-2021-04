package com.tpp.bhl

import org.jetbrains.exposed.dao.id.IntIdTable

object EnterEvent: IntIdTable() {

    val conveyUUID = varchar("conveyUUID", 36)

    val timestamp = long("timestamp")
}

object ExitEvent: IntIdTable() {

    val conveyUUID = varchar("conveyUUID", 36)

    val timestamp = long("timestamp")
}