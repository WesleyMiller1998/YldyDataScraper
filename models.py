import sqlite3
from sqlite3 import Error


def sql_connection():
    """Initiate connection to sqlite db."""

    try:
        conn = sqlite3.connect("ydly.db")
        return conn
    except Error:
        print(Error)


def create_database():
    conn = sql_connection()
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS accounts(address TEXT PRIMARY KEY, algoInAccount INT, yldyInAccount INT, algoStaked INT, yldyStaked INT)")
    conn.commit()
    c.close()


def insert_account(address, yldyInAccount, algoInAccount=None, algoStaked=None, yldyStaked=None):
    conn = sql_connection()
    c = conn.cursor()
    c.execute("INSERT INTO accounts VALUES (?,?,?,?,?)",
              (address, algoInAccount, yldyInAccount, algoStaked, yldyStaked))
    conn.commit()
    c.close()


def insert_yldy_balances(balances):
    vals = []

    for balance in balances:
        vals.append([balance["address"], None, balance["amount"], None, None])

    conn = sql_connection()
    c = conn.cursor()
    c.executemany("INSERT INTO accounts VALUES (?,?,?,?,?)",
                  vals)
    conn.commit()
    c.close()


def set_algo_in_account(address, algo):
    conn = sql_connection()
    c = conn.cursor()
    c.execute("UPDATE accounts SET algoInAccount = ? WHERE address = ?",
              (algo, address,))
    conn.commit()
    c.close()


def set_algo_staked(address, algoStaked):
    conn = sql_connection()
    c = conn.cursor()
    c.execute("UPDATE accounts SET algoStaked = ? WHERE address = ?",
              (algoStaked, address,))
    conn.commit()
    c.close()


def set_yldy_staked(address, yldyStaked):
    conn = sql_connection()
    c = conn.cursor()
    c.execute("UPDATE accounts SET yldyStaked = ? WHERE address = ?",
              (yldyStaked, address,))
    conn.commit()
    c.close()


def fetch_account(address):
    conn = sql_connection()
    c = conn.cursor()
    c.execute(
        "SELECT * FROM accounts WHERE address = ?", (address,))
    results = c.fetchone()
    c.close()
    return results


def fetch_account_like(phrase):
    conn = sql_connection()
    c = conn.cursor()
    c.execute(
        "SELECT * FROM accounts WHERE address LIKE '" + phrase + "%'")
    results = c.fetchone()
    c.close()
    return results


def delete_account(address):
    conn = sql_connection()
    c = conn.cursor()
    c.execute(
        "DELETE FROM accounts WHERE address = ?", (address,))
    results = c.fetchone()
    c.close()
    return results


def fetch_accounts():
    conn = sql_connection()
    c = conn.cursor()
    c.execute("SELECT address FROM accounts")
    results = c.fetchall()
    c.close()
    return results


def fetch_yldy_greater_than(x):
    conn = sql_connection()
    c = conn.cursor()
    c.execute(
        "SELECT * FROM accounts WHERE yldyInAccount + yldyStaked > ? ORDER BY yldyStaked DESC", (x * 1000000,))
    results = c.fetchall()
    c.close()
    return results


def fetch_all():
    conn = sql_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM accounts")
    results = c.fetchall()
    c.close()
    return results


def num_accounts():
    conn = sql_connection()
    c = conn.cursor()
    c.execute("SELECT count(*) FROM accounts")
    results = c.fetchone()[0]
    c.close()
    return results


def num_accounts_yldy_above(x):
    conn = sql_connection()
    c = conn.cursor()
    c.execute(
        "SELECT count(*) FROM accounts WHERE yldyInAccount + yldyStaked > ?", (x * 1000000,))
    results = c.fetchone()[0]
    c.close()
    return results


def sum_yldy_above(x):
    conn = sql_connection()
    c = conn.cursor()
    c.execute("SELECT sum(yldyInAccount + yldyStaked) FROM accounts WHERE yldyInAccount + yldyStaked > ?", (x * 1000000,))
    results = c.fetchone()[0]
    c.close()
    return results


def sum_unstaked_yldy():
    conn = sql_connection()
    c = conn.cursor()
    c.execute("SELECT sum(yldyInAccount) FROM accounts")
    results = c.fetchone()[0]
    c.close()
    return results


def sum_staked_yldy():
    conn = sql_connection()
    c = conn.cursor()
    c.execute("SELECT sum(yldyStaked) FROM accounts")
    results = c.fetchone()[0]
    c.close()
    return results


def fetch_top(x):
    conn = sql_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM accounts ORDER BY yldyStaked DESC LIMIT ?", (x,))
    results = c.fetchall()
    c.close()
    return results


def fetch_top_yldy(x):
    conn = sql_connection()
    c = conn.cursor()
    c.execute(
        "SELECT * FROM accounts ORDER BY yldyInAccount + yldyStaked DESC LIMIT ?", (x,))
    results = c.fetchall()
    c.close()
    return results


def fetch_top_algo(x):
    conn = sql_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM accounts WHERE yldyInAccount > 0 OR yldyStaked > 0 ORDER BY algoStaked DESC LIMIT ?", (x,))
    results = c.fetchall()
    c.close()
    return results


def fetch_all_yldy_desc():
    conn = sql_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM accounts ORDER BY yldyStaked DESC")
    results = c.fetchall()
    c.close()
    return results
