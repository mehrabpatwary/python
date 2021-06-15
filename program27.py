studentId = {
    '101': 'Mehrab Patwary',
    '102': 'Toma Tohura',
    '103': 'Anika Zaman',
    '104': 'Anisul Islam',
    105: 'Tasnova Tarin'
}
print(studentId['101'])
print(studentId.get('104'))
print(studentId.get('105'))
print(studentId.get('105', 'Not a valid key'))
print(studentId.get('102', 'Not a valid key'))
print(studentId.get(105, 'Not a valid key'))
