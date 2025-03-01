'''
HW5 pandas exercises (Task3).
'''

import sys
import pandas as pd

# ====== Task3

# load data
cities    = pd.read_csv('data_nba/cities.csv')
players   = pd.read_csv('data_nba/players.csv')
teams     = pd.read_csv('data_nba/teams.csv')
divisions = pd.read_csv('data_nba/divisions.csv')
games     = pd.read_csv('data_nba/games.csv')
box       = pd.read_csv('data_nba/box.csv')

# [[[ TODO a) players_by_name_fragment ]]]

# get players by fragment of a name
def players_by_name_fragment(fragment: str) -> pd.DataFrame:
    '''
    Return a DataFrame containing columns 'personId' and 'personName'.

    All players whose name contains the given fragment, case
    insensitive, must appear in the result.
    '''
    raise NotImplementedError('players_by_name_fragment')

# [[[ TODO b) ppg_by_player ]]]

def ppg_by_name(name: str) -> float:
    '''
    PPG stands for "points per game."

    Return the points per game for the given player whose name is
    exactly the given string, case sensitive. Please note that every
    player name in the data set is unique, so you need not worry
    about accidentally combining data from multiple players.

    Raise a ValueError if there is no such player.
    '''
    raise NotImplementedError('ppg_by_name')

# [[[ TODO c) played_for ]]]

def played_for(team: str) -> pd.DataFrame:
    '''
    Return a DataFrame containing columns 'personId' and
    'personName'. The result must contain no duplicate rows.

    The argument 'team' is a string like 'CHI' or 'MIN'.

    Raise a ValueError if the team does not exist.
    '''
    raise NotImplementedError('played_for')

# [[[ TODO d) top_n_scorers_by_team ]]]

def top_n_scorers_by_team(team: str, n: int) -> pd.DataFrame:
    '''
    Return a DataFrame containing columns 'personId',
    'personName', and 'ppg'.

    Return the top n scorers for the given team by ppg. If n exceeds
    the number of scorers for that team, return as many as there are.

    Raise a ValueError if the team does not exist of if n<1.
    '''
    raise NotImplementedError('top_n_scorers_by_team')

# [[[ TODO e) played_on_both ]]]

def played_on_both(team1: str, team2: str) -> set[str]:
    '''
    Return a set of strings, where each string is a player's name, for
    all players who have played on both team1 and team2.

    Raise a ValueError if either team does not exist.
    '''
    raise NotImplementedError('played_on_both')

# [[[ TODO f) top_n_scorers_by_division ]]]

def top_n_scorers_by_division(division: str, n: int) -> pd.DataFrame:
    '''
    Return a DataFrame containing columns 'personId',
    'personName', and 'ppg'.

    Return the top n scorers for the given division by ppg. If n exceeds
    the number of scorers for that division, return as many as there are.

    Raise a ValueError if the division does not exist or if n<1.
    '''
    raise NotImplementedError('top_n_scorers_by_division')

# [[[ TODO g)  played_on_date ]]]

def played_on_date(date: str) -> set[str]:
    '''
    Return a set of player names for players who played on given
    date according to the data set.

    The date format is a YYYY-MM-DD string like '2024-02-03' (which is
    what is in the given CSV files).

    Answering this question requires inspecting the contents of games, box, and
    players, all three -- a Pandas 'merge' is recommended.

    It is not necessary to test that the date is in a particular span
    of time or that it is well-formatted; the function caller is
    responsible for supplying a reasonable date.

    '''
    raise NotImplementedError('played_on_date')
