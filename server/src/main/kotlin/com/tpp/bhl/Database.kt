package com.tpp.bhl

import org.jetbrains.exposed.sql.Database
import org.jetbrains.exposed.sql.SchemaUtils
import org.jetbrains.exposed.sql.Transaction
import org.jetbrains.exposed.sql.transactions.transaction

object Database {

    private val db by lazy {
        Database.connect(
            url = Env.getDbUrl(),
            driver = "org.postgresql.Driver",
            user = Env.getDbUser(),
            password = Env.getDbPassword()
        )
    }

    fun <T> execute(statement: Transaction.() -> T) {
        evaluate(statement)
    }

    fun <T> evaluate(statement: Transaction.() -> T): T = transaction(db, statement)

    fun initTables() = execute {
        SchemaUtils.createMissingTablesAndColumns(
            EnterEvent,
            ExitEvent,
            ResetEvent
        )
    }
}