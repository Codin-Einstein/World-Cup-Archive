"""Seed the World Cup database with tournament, team, match, and moment data."""
import sqlite3
import os
from pathlib import Path

DB_PATH = Path(__file__).parent / "worldcup.db"

teams = [
    ("Uruguay", "URU"), ("Argentina", "ARG"), ("Brazil", "BRA"), ("Italy", "ITA"),
    ("Germany", "GER"), ("France", "FRA"), ("England", "ENG"), ("Spain", "ESP"),
    ("Netherlands", "NED"), ("West Germany", "FRG"), ("Portugal", "POR"),
    ("Croatia", "CRO"), ("Sweden", "SWE"), ("Hungary", "HUN"),
    ("Czechoslovakia", "TCH"), ("Austria", "AUT"), ("Switzerland", "SUI"),
    ("Soviet Union", "URS"), ("Poland", "POL"), ("Turkey", "TUR"),
    ("Yugoslavia", "YUG"), ("Chile", "CHI"), ("Belgium", "BEL"),
    ("United States", "USA"), ("South Korea", "KOR"), ("Japan", "JPN"),
    ("Morocco", "MAR"), ("Senegal", "SEN"), ("Colombia", "COL"), ("Denmark", "DEN"),
    ("Mexico", "MEX"), ("Paraguay", "PAR"), ("Cameroon", "CMR"), ("Nigeria", "NGA"),
    ("Ghana", "GHA"), ("Costa Rica", "CRC"), ("Saudi Arabia", "KSA"), ("Iran", "IRN"),
    ("Australia", "AUS"), ("Romania", "ROU"), ("Bulgaria", "BUL"), ("Scotland", "SCO"),
    ("Northern Ireland", "NIR"), ("Wales", "WAL"), ("Algeria", "ALG"),
    ("Ivory Coast", "CIV"), ("Tunisia", "TUN"), ("Egypt", "EGY"), ("Ecuador", "ECU"),
    ("Peru", "PER"), ("Honduras", "HON"), ("New Zealand", "NZL"), ("Iraq", "IRQ"),
    ("Kuwait", "KUW"), ("Canada", "CAN"), ("Cuba", "CUB"), ("Dutch East Indies", "DEI"),
    ("Norway", "NOR"), ("Ireland", "IRL"), ("Bosnia", "BIH"), ("Ukraine", "UKR"),
    ("Serbia", "SRB"), ("Czech Republic", "CZE"), ("Russia", "RUS"), ("Panama", "PAN"),
    ("Iceland", "ISL"), ("Qatar", "QAT"), ("Serbia and Montenegro", "SCG"),
    ("Zaire", "ZAI"), ("Haiti", "HAI"), ("East Germany", "GDR"), ("El Salvador", "SLV"),
    ("Zambia", "ZAM"), ("Indonesia", "IDN"), ("United Arab Emirates", "UAE"),
    ("Jamaica", "JAM"), ("South Africa", "RSA"), ("China", "CHN"), ("Togo", "TOG"),
    ("Trinidad and Tobago", "TRI"), ("Angola", "ANG"), ("Slovakia", "SVK"),
    ("Slovenia", "SVN"),
]

tournaments = [
    (1930, "Uruguay", "Uruguay", "Argentina", "United States", "Yugoslavia", 70, 18, 590549),
    (1934, "Italy", "Italy", "Czechoslovakia", "Germany", "Austria", 70, 17, 363000),
    (1938, "France", "Italy", "Hungary", "Brazil", "Sweden", 84, 18, 375700),
    (1950, "Brazil", "Uruguay", "Brazil", "Sweden", "Spain", 88, 22, 1045246),
    (1954, "Switzerland", "West Germany", "Hungary", "Austria", "Uruguay", 140, 26, 768607),
    (1958, "Sweden", "Brazil", "Sweden", "France", "West Germany", 126, 35, 819810),
    (1962, "Chile", "Brazil", "Czechoslovakia", "Chile", "Yugoslavia", 89, 32, 893172),
    (1966, "England", "England", "West Germany", "Portugal", "Soviet Union", 89, 32, 1563135),
    (1970, "Mexico", "Brazil", "Italy", "West Germany", "Uruguay", 95, 32, 1603975),
    (1974, "West Germany", "West Germany", "Netherlands", "Poland", "Brazil", 97, 38, 1865753),
    (1978, "Argentina", "Argentina", "Netherlands", "Brazil", "Italy", 102, 38, 1545791),
    (1982, "Spain", "Italy", "West Germany", "Poland", "France", 146, 52, 2109723),
    (1986, "Mexico", "Argentina", "West Germany", "France", "Belgium", 132, 52, 2394031),
    (1990, "Italy", "West Germany", "Argentina", "Italy", "England", 115, 52, 2516215),
    (1994, "United States", "Brazil", "Italy", "Sweden", "Bulgaria", 141, 52, 3587538),
    (1998, "France", "France", "Brazil", "Croatia", "Netherlands", 171, 64, 2785100),
    (2002, "South Korea/Japan", "Brazil", "Germany", "Turkey", "South Korea", 161, 64, 2705197),
    (2006, "Germany", "Italy", "France", "Germany", "Portugal", 147, 64, 3359439),
    (2010, "South Africa", "Spain", "Netherlands", "Germany", "Uruguay", 145, 64, 3178856),
    (2014, "Brazil", "Germany", "Argentina", "Netherlands", "Brazil", 171, 64, 3429873),
    (2018, "Russia", "France", "Croatia", "Belgium", "England", 169, 64, 3031768),
    (2022, "Qatar", "Argentina", "France", "Croatia", "Morocco", 172, 64, 3404252),
]

famous_matches = [
    (1950, "Final Round", "1950-07-16", "Uruguay", "Brazil", 2, 1, "Uruguay", "Maracanã Stadium", "Rio de Janeiro", 173850),
    (1954, "Final", "1954-07-04", "West Germany", "Hungary", 3, 2, "West Germany", "Wankdorf Stadium", "Bern", 62500),
    (1958, "Final", "1958-06-29", "Brazil", "Sweden", 5, 2, "Brazil", "Råsunda Stadium", "Stockholm", 51700),
    (1966, "Final", "1966-07-30", "England", "West Germany", 4, 2, "England", "Wembley Stadium", "London", 96924),
    (1970, "Final", "1970-06-21", "Brazil", "Italy", 4, 1, "Brazil", "Estadio Azteca", "Mexico City", 107412),
    (1970, "Semi-final", "1970-06-17", "Italy", "West Germany", 4, 3, "Italy", "Estadio Azteca", "Mexico City", 102444),
    (1974, "Final", "1974-07-07", "Netherlands", "West Germany", 1, 2, "West Germany", "Olympiastadion", "Munich", 78200),
    (1978, "Final", "1978-06-25", "Argentina", "Netherlands", 3, 1, "Argentina", "Estadio Monumental", "Buenos Aires", 71483),
    (1982, "Semi-final", "1982-07-08", "West Germany", "France", 3, 3, "West Germany", "Estadio Ramón Sánchez Pizjuán", "Seville", 63000),
    (1986, "Quarter-final", "1986-06-22", "Argentina", "England", 2, 1, "Argentina", "Estadio Azteca", "Mexico City", 114580),
    (1986, "Final", "1986-06-29", "Argentina", "West Germany", 3, 2, "Argentina", "Estadio Azteca", "Mexico City", 114600),
    (1990, "Semi-final", "1990-07-03", "Argentina", "Italy", 1, 1, "Argentina", "Stadio San Paolo", "Naples", 59517),
    (1994, "Final", "1994-07-17", "Brazil", "Italy", 0, 0, "Brazil", "Rose Bowl", "Pasadena", 94194),
    (1998, "Final", "1998-07-12", "France", "Brazil", 3, 0, "France", "Stade de France", "Saint-Denis", 80000),
    (2002, "Final", "2002-06-30", "Germany", "Brazil", 0, 2, "Brazil", "International Stadium", "Yokohama", 69029),
    (2002, "Round of 16", "2002-06-18", "South Korea", "Italy", 2, 1, "South Korea", "Daejeon World Cup Stadium", "Daejeon", 38588),
    (2006, "Final", "2006-07-09", "Italy", "France", 1, 1, "Italy", "Olympiastadion", "Berlin", 69000),
    (2010, "Final", "2010-07-11", "Netherlands", "Spain", 0, 1, "Spain", "Soccer City", "Johannesburg", 84490),
    (2014, "Semi-final", "2014-07-08", "Brazil", "Germany", 1, 7, "Germany", "Estádio Mineirão", "Belo Horizonte", 58241),
    (2014, "Final", "2014-07-13", "Germany", "Argentina", 1, 0, "Germany", "Maracanã Stadium", "Rio de Janeiro", 74738),
    (2018, "Round of 16", "2018-06-30", "France", "Argentina", 4, 3, "France", "Kazan Arena", "Kazan", 42873),
    (2018, "Final", "2018-07-15", "France", "Croatia", 4, 2, "France", "Luzhniki Stadium", "Moscow", 78011),
    (2022, "Final", "2022-12-18", "Argentina", "France", 3, 3, "Argentina", "Lusail Iconic Stadium", "Lusail", 88966),
    (2022, "Quarter-final", "2022-12-09", "Netherlands", "Argentina", 2, 2, "Argentina", "Lusail Iconic Stadium", "Lusail", 88835),
    (2022, "Quarter-final", "2022-12-10", "Morocco", "Portugal", 1, 0, "Morocco", "Al Thumama Stadium", "Doha", 68323),
    (1998, "Quarter-final", "1998-07-04", "Netherlands", "Argentina", 2, 1, "Netherlands", "Stade Vélodrome", "Marseille", 60000),
    (2006, "Semi-final", "2006-07-05", "Portugal", "France", 0, 1, "France", "Allianz Arena", "Munich", 66000),
    (2010, "Quarter-final", "2010-07-02", "Uruguay", "Ghana", 1, 1, "Uruguay", "Soccer City", "Johannesburg", 84017),
    (2018, "Quarter-final", "2018-07-07", "Russia", "Croatia", 2, 2, "Croatia", "Fisht Olympic Stadium", "Sochi", 44287),
    (1990, "Group Stage", "1990-06-08", "Argentina", "Cameroon", 0, 1, "Cameroon", "San Siro", "Milan", 73780),
    (1966, "Group Stage", "1966-07-13", "Portugal", "Hungary", 3, 1, "Portugal", "Old Trafford", "Manchester", 37000),
    (1930, "Final", "1930-07-30", "Uruguay", "Argentina", 4, 2, "Uruguay", "Estadio Centenario", "Montevideo", 68346),
    (1934, "Final", "1934-06-10", "Italy", "Czechoslovakia", 2, 1, "Italy", "Stadio Nazionale PNF", "Rome", 55000),
    (1938, "Final", "1938-06-19", "Italy", "Hungary", 4, 2, "Italy", "Stade Olympique de Colombes", "Paris", 45000),
    (1962, "Final", "1962-06-17", "Brazil", "Czechoslovakia", 3, 1, "Brazil", "Estadio Nacional", "Santiago", 68679),
    (1958, "Quarter-final", "1958-06-19", "Brazil", "Wales", 1, 0, "Brazil", "Nya Ullevi", "Gothenburg", 25000),
    (1982, "Second Round", "1982-07-05", "Italy", "Brazil", 3, 2, "Italy", "Estadio de Sarrià", "Barcelona", 44000),
    (1954, "Group Stage", "1954-06-20", "Hungary", "West Germany", 8, 3, "Hungary", "St. Jakob Stadium", "Basel", 56000),
    (1978, "Second Round", "1978-06-21", "Argentina", "Peru", 6, 0, "Argentina", "Estadio Gigante de Arroyito", "Rosario", 37315),
    (1994, "Quarter-final", "1994-07-09", "Netherlands", "Brazil", 2, 3, "Brazil", "Cotton Bowl", "Dallas", 63500),
    (2002, "Group Stage", "2002-05-31", "France", "Senegal", 0, 1, "Senegal", "Seoul World Cup Stadium", "Seoul", 62500),
    (2010, "Quarter-final", "2010-07-03", "Argentina", "Germany", 0, 4, "Germany", "Cape Town Stadium", "Cape Town", 64100),
    (2022, "Group Stage", "2022-11-23", "Germany", "Japan", 1, 2, "Japan", "Khalifa International Stadium", "Al Rayyan", 42508),
    (2022, "Group Stage", "2022-11-22", "Argentina", "Saudi Arabia", 1, 2, "Saudi Arabia", "Lusail Iconic Stadium", "Lusail", 88012),
]

moments_data = [
    (0, "Maracanazo - Uruguay stun Brazil at home", "Uruguay beats Brazil 2-1 in the decisive final round match at the Maracanã, one of the biggest upsets in history.", "https://www.youtube.com/embed/Pu1WanatiAM", "iconic"),
    (1, "Miracle of Bern - West Germany win first title", "West Germany come from 2-0 down to beat Hungary 3-2 in the 1954 final.", "https://www.youtube.com/embed/2qCZe6Ki-zk", "iconic"),
    (2, "Pelé makes his mark - 1958 World Cup Final", "17-year-old Pelé scores two goals in the final as Brazil beats Sweden 5-2.", "https://www.youtube.com/embed/JE2xPzeSiBc", "legend"),
    (3, "England's finest hour - 1966 World Cup Final", "Geoff Hurst scores a hat-trick as England beats West Germany 4-2 at Wembley.", "https://www.youtube.com/embed/FMDuHPvNtgg", "iconic"),
    (4, "Brazil's eternal trophy - 1970 Final", "Brazil beats Italy 4-1 to win the Jules Rimet trophy for the third time.", "https://www.youtube.com/embed/kBJVZ5k-F3M", "legend"),
    (5, "Game of the Century - Italy 4-3 West Germany", "Five goals in extra time in one of the greatest matches ever played at the 1970 World Cup semi-final.", "https://www.youtube.com/embed/x17DPctOATY", "classic"),
    (6, "Cruyff's Dutch revolution - 1974 Final", "Netherlands' Total Football meets West Germany in the 1974 final.", "https://www.youtube.com/embed/qSznZ9spb6A", "classic"),
    (7, "Argentina's first title - 1978 Final", "Argentina beats Netherlands 3-1 with Kempes scoring twice in front of a packed Monumental.", "https://www.youtube.com/embed/2EwfHjbeNV8", "iconic"),
    (8, "Hand of God & Goal of the Century", "Maradona scores both the 'Hand of God' and the 'Goal of the Century' in the same match against England.", "https://www.youtube.com/embed/FRAbNlPS2MI", "legend"),
    (9, "Maradona lifts the trophy - 1986 Final", "Argentina beats West Germany 3-2 as Maradona cements his legacy.", "https://www.youtube.com/embed/WQ2V1DlefW0", "iconic"),
    (10, "Baggio skies it - 1994 Final", "Brazil beats Italy on penalties after a 0-0 draw. Roberto Baggio famously misses the decisive penalty.", "https://www.youtube.com/embed/pLPM_JSbGvI", "drama"),
    (11, "Argentina stun hosts Italy in Naples", "Argentina beats Italy on penalties in the 1990 semi-final, played in Maradona's adopted home.", "https://www.youtube.com/embed/oiC4YMG8raQ", "drama"),
    (12, "France conquer the world - 1998 Final", "Zidane scores twice as France beats Brazil 3-0 in Paris.", "https://www.youtube.com/embed/tmjFa9LB7Pg", "iconic"),
    (13, "Ronaldo redemption - 2002 Final", "Ronaldo scores twice to lead Brazil past Germany 2-0, exorcising the demons of 1998.", "https://www.youtube.com/embed/O8dUhMGtUtw", "iconic"),
    (14, "Zidane's headbutt - 2006 Final", "Zidane is sent off for headbutting Materazzi in extra time. Italy wins on penalties.", "https://www.youtube.com/embed/Nlsm0RlC8zI", "drama"),
    (15, "Iniesta writes history - 2010 Final", "Andrés Iniesta scores in extra time to give Spain their first World Cup title.", "https://www.youtube.com/embed/aKSHgMqCwbQ", "iconic"),
    (16, "Mineirazo - Germany humiliate Brazil 7-1", "Germany scores 5 goals in 6 minutes destroying Brazil 7-1 in the semi-final.", "https://www.youtube.com/embed/aE4BdIP6bvc", "historic"),
    (17, "Götze's magic moment - 2014 Final", "Mario Götze scores a stunning extra-time winner to give Germany the title over Argentina.", "https://www.youtube.com/embed/ffAYByv2pLc", "iconic"),
    (18, "Mbappé announces himself - France 4-3 Argentina", "19-year-old Mbappé terrorizes Argentina in a 4-3 thriller in the Round of 16.", "https://www.youtube.com/embed/6C6oOcDFmLY", "classic"),
    (19, "France victorious again - 2018 Final", "France beats Croatia 4-2 in a goal-filled final in Moscow.", "https://www.youtube.com/embed/GrsEAvRerTg", "iconic"),
    (20, "The greatest final ever - Argentina 3-3 France", "Messi vs Mbappé in an all-time classic. Messi finally wins the World Cup.", "https://www.youtube.com/embed/zhEWqfP6V_w", "legend"),
    (21, "Morocco makes history - first African semi-finalist", "Morocco beats Portugal 1-0 to become the first African team to reach the World Cup semi-finals.", "https://www.youtube.com/embed/M766FGsv5do", "historic"),
    (22, "Suárez handball - Uruguay vs Ghana 2010", "Luis Suárez handles the ball on the line, gets sent off, but Ghana miss the penalty.", "https://www.youtube.com/embed/tDpx9GGH79I", "drama"),
    (23, "Bergkamp's masterpiece - 1998", "Bergkamp scores an iconic goal in the dying seconds to beat Argentina in the quarter-final.", "https://www.youtube.com/embed/DemI2OO7FsU", "legend"),
    (24, "Italy vs Brazil 3-2 - 1982 classic", "Paolo Rossi scores a hat-trick as Italy beats Brazil 3-2 in one of the greatest matches ever.", "https://www.youtube.com/embed/yBC02hKBTlQ", "classic"),
    (25, "Hungary 8-3 West Germany - group stage classic", "Hungary demolishes West Germany 8-3, only to lose to them in the final.", "https://www.youtube.com/embed/7KQc2W8DNog", "classic"),
    (26, "Senegal stun France in 2002 opener", "Defending champions France lose 1-0 to Senegal in the opening match.", "https://www.youtube.com/embed/NZ7Cdw-zO0M", "drama"),
    (27, "Japan shock Germany 2-1 - 2022", "Japan come from behind to beat Germany 2-1 in one of the biggest 2022 World Cup upsets.", "https://www.youtube.com/embed/fXVWZS76QyE", "drama"),
    (28, "Saudi Arabia stun Argentina - 2022", "Saudi Arabia pull off one of the greatest upsets in World Cup history, beating Messi's Argentina 2-1.", "https://www.youtube.com/embed/spLV1gF0fkI", "historic"),
    (29, "Cameroon beat Argentina - 1990 opener", "Defending champions Argentina shocked by Cameroon in the 1990 World Cup opener.", "https://www.youtube.com/embed/tSXoVcI1mK4", "drama"),
]


def seed():
    if DB_PATH.exists():
        os.remove(DB_PATH)

    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS tournaments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            year INTEGER NOT NULL UNIQUE,
            host TEXT NOT NULL,
            winner TEXT NOT NULL,
            runner_up TEXT NOT NULL,
            third_place TEXT,
            fourth_place TEXT,
            total_goals INTEGER,
            total_matches INTEGER,
            attendance INTEGER
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            country_code TEXT NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tournament_id INTEGER NOT NULL,
            stage TEXT NOT NULL,
            date TEXT NOT NULL,
            team1_id INTEGER NOT NULL,
            team2_id INTEGER NOT NULL,
            score_team1 INTEGER,
            score_team2 INTEGER,
            winner_id INTEGER,
            venue TEXT,
            city TEXT,
            attendance INTEGER,
            FOREIGN KEY (tournament_id) REFERENCES tournaments(id),
            FOREIGN KEY (team1_id) REFERENCES teams(id),
            FOREIGN KEY (team2_id) REFERENCES teams(id),
            FOREIGN KEY (winner_id) REFERENCES teams(id)
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS moments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            match_id INTEGER,
            title TEXT NOT NULL,
            description TEXT,
            video_url TEXT NOT NULL,
            source TEXT DEFAULT 'YouTube',
            category TEXT DEFAULT 'highlight',
            FOREIGN KEY (match_id) REFERENCES matches(id)
        )
    """)

    team_map = {}
    for name, code in teams:
        cur.execute("INSERT INTO teams (name, country_code) VALUES (?, ?)", (name, code))
        team_map[name] = cur.lastrowid

    tournament_map = {}
    for t in tournaments:
        cur.execute(
            "INSERT INTO tournaments (year, host, winner, runner_up, third_place, fourth_place, total_goals, total_matches, attendance) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            t,
        )
        tournament_map[t[0]] = cur.lastrowid

    match_ids = []
    for m in famous_matches:
        cur.execute(
            "INSERT INTO matches (tournament_id, stage, date, team1_id, team2_id, score_team1, score_team2, winner_id, venue, city, attendance) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                tournament_map[m[0]], m[1], m[2],
                team_map[m[3]], team_map[m[4]],
                m[5], m[6], team_map[m[7]],
                m[8], m[9], m[10],
            ),
        )
        match_ids.append(cur.lastrowid)

    for idx, title, desc, video_url, category in moments_data:
        match_id = match_ids[idx]
        cur.execute(
            "INSERT INTO moments (match_id, title, description, video_url, category) VALUES (?, ?, ?, ?, ?)",
            (match_id, title, desc, video_url, category),
        )

    conn.commit()
    conn.close()

    print(f"Seeded {len(teams)} teams, {len(tournaments)} tournaments, {len(famous_matches)} matches, {len(moments_data)} moments.")


if __name__ == "__main__":
    seed()
