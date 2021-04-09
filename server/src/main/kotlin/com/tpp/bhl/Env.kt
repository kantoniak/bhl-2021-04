package com.tpp.bhl

object Env {

    fun getServerPort(defaultPort: Int = 8080): Int =
        System.getenv("PORT")?.toInt() ?: defaultPort

    fun getDbUrl(defaultUrl: String = "jdbc:postgresql://localhost:5432/"): String =
        System.getenv("JDBC_DATABASE_URL") ?: defaultUrl

    fun getDbUser(defaultUser: String = "postgres"): String =
        System.getenv("JDBC_DATABASE_USERNAME") ?: defaultUser

    fun getDbPassword(defaultPassword: String = "postgres"): String =
        System.getenv("JDBC_DATABASE_PASSWORD") ?: defaultPassword
}