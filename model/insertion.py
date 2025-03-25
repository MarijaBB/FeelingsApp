import mysql.connector
from datetime import datetime


mydb = mysql.connector.connect(
  host='localhost',
  user='',     # not showing publicly
  password='', # not showing publicly
  database = 'feelDB'
)

mycursor = mydb.cursor()
#mycursor.execute('ALTER TABLE Messages DROP COLUMN ColorCode')

sql1 = 'INSERT INTO Feelings (Title, Image, ColorCode) VALUES (%s,%s,%s)'
val1 = [
('happy',' ./images/happy.jpg', 'orange'),
('sad', './images/sad.jpg', 'green'),
('angry', './images/angry.jpg', 'blue'),
('bored', './images/bored.jpg', 'green'),
('calm', './images/calm.jpg','orange'),
( 'concerned', './images/concerned.jpg','green'),
('determined', './images/determined.jpg','orange'),
( 'funky', './images/funky.jpg','orange'),
('overstimulated', './images/overstimulated.png','blue'),
( 'socially anxious', './images/socially anxious.jpg','green'),
('tired', './images/tired.png','blue')
]



sql2 = 'INSERT INTO Users (UserName,Email,PasswordHash, CreatedAt) VALUES (%s,%s,%s,%s)'
val2 = [('Marija', 'test@gmail.com','test', datetime.now())]

sql3 = 'INSERT INTO Messages (Message, FeelingId) VALUES (%s,%s)' 
val3 = [
('This tough time will pass, and brighter days are ahead.', 2),
('Every storm eventually clears, revealing the sunshine again.', 2),
('It\'s okay to feel sad sometimes. Emotions are part of the journey.', 2),
('Even small steps forward are signs of strength and progress.', 2),
('There is so much strength within. Keep going, one step at a time.', 2),
('Difficult moments often lead to the greatest growth.', 2),
('Take a deep breath and let hope fill the heart.', 2),
('A smile will find its way back, even if it takes time.', 2),
('Support and love are always around, even in tough times.', 2),
('Keep pushing forward—there is so much to look forward to.', 2),
('Take a deep breath and give yourself a moment to pause.', 3),
    ('Anger is temporary—focus on finding peace within.', 3),
    ('Step away for a bit and allow the mind to clear.', 3),
    ('Not every battle needs to be fought right now. Choose peace.', 3),
    ('Breathe in slowly, hold, and exhale. Let the tension fade away.', 3),
    ('A calm mind finds better solutions than an angry one.', 3),
    ('Let go of what can\'t be controlled and focus on what brings peace.', 3),
    ('Frustration is natural, but it doesn\'t have to control the day.', 3),
    ('Words said in anger are hard to take back—take a moment before responding.', 3),
    ('Redirect that energy into something positive. A clear mind leads to better outcomes.', 3),
    ('Happiness looks great on you! Keep shining.',1),
    ('Enjoy this moment—joy is meant to be felt fully.',1),
    ('Happiness is contagious—spread it everywhere!',1),
    ('Hold onto this feeling and let it brighten your days.',1),
    ('Every smile adds a little more light to the world.',1),
    ('Keep embracing the things that bring joy and laughter.',1),
    ('Let happiness be the fuel that keeps you moving forward.',1),
    ('Celebrate the good times, big or small!',1),
    ('Happiness grows when shared—let others feel the warmth too.',1),
    ('Stay present in this moment, and let joy fill your heart.',1),
    ('Boredom is just the universe nudging you to try something new. What\'s one small thing you can do differently today?', 4),
('Feeling bored? Maybe it\'s time to dive into a random fun fact or learn a weird skill!', 4),
('Boredom is a sign of untapped creativity. What\'s one small project or idea you can explore?', 4),
('Try stepping outside, stretching, or listening to a song you haven\'t heard before. Change the vibe!', 4),
('Your next adventure might be one decision away. What\'s something spontaneous you can do right now?', 4),

('Enjoy this moment of peace. Let it refill your energy for whatever comes next.', 5),
('Calmness is power. Stay in this moment and let it guide you forward.', 5),
('Breathe in, breathe out. Right now, everything is okay.', 5),
('A calm mind makes the best decisions. Keep that steady energy!', 5),
('You are in control. Enjoy the stillness and let it bring you clarity.', 5),

('It\'s okay to feel concerned. Acknowledge your thoughts, but don\'t let them take over.', 6),
('Worrying means you care. Focus on what you can control, and take it one step at a time.', 6),
('You don\'t have to figure everything out at once. Small steps can lead to big solutions.', 6),
('Talk it out with someone you trust—sometimes, an outside perspective helps ease the mind.', 6),
('Breathe. Stay present. You\'ve handled challenges before, and you\'ll get through this one too.', 6),

('You\'ve got this! Keep pushing forward—small steps lead to big victories.', 7),
('Determination fuels success. Stay focused, and trust the process.', 7),
('Your dedication is what sets you apart. Keep moving, and you\'ll get there!', 7),
('Every great achievement starts with determination. Stay strong, stay steady.', 7),
('Obstacles are just part of the journey. Keep going—you are unstoppable!', 7),

('Let your weirdness shine! The world needs your unique energy.', 8),
('Dance like nobody\'s watching, sing like nobody\'s listening. Funk it up!', 8),
('Being funky means living life on your terms. Own it!', 8),
('Your vibe is contagious—keep spreading the funk!', 8),
('Why fit in when you were born to stand out? Embrace your funky side!', 8),

('Take a deep breath. Step away from the noise and give yourself a moment to reset.', 9),
('Feeling overwhelmed? Try closing your eyes for a few seconds and focusing on your breath.', 9),
('It\'s okay to take a break. Your well-being comes first.', 9),
('Find a quiet space, put on some calming music, and allow yourself to decompress.', 9),
('The world can wait. Prioritize your peace and take things one step at a time.', 9),

('You are not alone in this feeling. Breathe deeply and take it one moment at a time.', 10),
('You don\'t have to say the perfect thing—just being present is enough.', 10),
('It\'s okay to step away and take a break. Your comfort matters.', 10),
('You are worthy of connection. The right people will appreciate you as you are.', 10),
('Remember, most people are too busy with their own thoughts to judge you. Just be yourself!', 10),

('Rest is productive too. Give yourself the break you deserve.', 11),
('You\'ve done enough today. It\'s okay to recharge and come back stronger.', 11),
('Sleep, water, and kindness to yourself—your body and mind will thank you.', 11),
('Sometimes the best thing you can do is close your eyes and let yourself rest.', 11),
('Energy will return, but for now, allow yourself to slow down and breathe.', 11)
];


mycursor.executemany(sql1, val1)
mycursor.executemany(sql2, val2)
mycursor.executemany(sql3, val3)

mydb.commit()
