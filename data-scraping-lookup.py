import sqlite3


db = 'assets/stars.db'
class Star:
    def __init__(self, name):
        self.name = name
        self.not_found = False
        if not self._lookup_en() and not self._lookup_cn():
            self.not_found = True
        
    def _lookup(self, colname):
        try:
            conn = sqlite3.connect(db)
            cur = conn.cursor()
            sql = f'SELECT stars.name, stars.name_cn, stars.magnitude, cons.name, cons.name_cn FROM stars LEFT JOIN cons ON cons.abbr WHERE stars.{colname} LIKE ? ORDER BY stars.top20 DESC, stars.magnitude'
            cur.execute(sql, ('%' + self.name + '%',))
            result = cur.fetchone()
            if result:
                self.name, self.name_cn, self.magnitude, self.cons_name, self.cons_name_cn = result
                return True
            else:
                return False
        finally:
            conn.close()
    
    def _lookup_en(self):
        return self._lookup('name')
    
    def _lookup_cn(self):
        return self._lookup('name_cn')

    def __str__(self):
        if self.not_found:
            return f'{self.name}: not found'
        return f'{self.name} in {self.cons_name}: {self.cons_name_cn} 的 {self.name_cn}，视星等{self.magnitude}'
    
    __repr__ = __str__

print(Star('摩羯座'))
