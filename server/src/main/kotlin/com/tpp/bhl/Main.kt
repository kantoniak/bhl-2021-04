package com.tpp.bhl

import io.javalin.Javalin
import io.javalin.apibuilder.ApiBuilder.*

data class StringData(val id: Long, val data: String)

class StringDao {

    val strings: MutableList<StringData> = mutableListOf() // Server starts with empty list

    fun addStringData(data: StringData) {
        strings.add(data)
    }

    fun removeStringData(stringId: Long): Boolean = strings.removeIf { it.id == stringId }
}

fun main() {
    val stringDao = StringDao()

    val app = Javalin.create().apply {
        exception(Exception::class.java) { e, _ -> e.printStackTrace() }
    }.start("0.0.0.0", getEnvPort())

    app.routes {
        get("/strings") { context ->
            context.json(stringDao.strings)
        }

        post("/strings") { context ->
            val stringData = context.body<StringData>()
            stringDao.addStringData(stringData)
            context.status(201)
        }

        delete("/strings/:stringId") { context ->
            stringDao.removeStringData(context.pathParam("stringId").toLongOrNull() ?: -1).let {
                if (it)
                    context.status(204)
                else
                    context.status(400)
            }
        }
    }
}

private fun getEnvPort(defaultPort: Int = 8080): Int {
    val herokuPort = System.getenv("PORT")
    return herokuPort?.toInt() ?: defaultPort
}