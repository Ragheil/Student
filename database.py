def Database():
    conn = sqlite3.connect("masterfile.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `masterfile` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, number TEXT, sname TEXT, gender TEXT, course TEXT, subject TEXT, prelim TEXT, midterm TEXT, final TEXT, average TEXT, pequivalent TEXT, remarks TEXT)")
    cursor.execute("SELECT * FROM `masterfile` ORDER BY `number` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()