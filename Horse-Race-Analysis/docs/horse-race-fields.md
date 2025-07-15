# Horse Race Data Fields Documentation

This document explains all the fields (features) in the horse race dataset (`field.csv`). The dataset contains comprehensive information about horse racing, including race details, horse characteristics, performance statistics, and betting information.

## Table of Contents
- [Race Information](#race-information)
- [Horse Identification](#horse-identification)
- [Race Participants](#race-participants)
- [Horse Demographics](#horse-demographics)
- [Performance Statistics](#performance-statistics)
- [Race Conditions](#race-conditions)
- [Betting Information](#betting-information)
- [Recent Performance](#recent-performance)
- [Track and Distance](#track-and-distance)
- [Additional Features](#additional-features)

## Race Information

### Venue
- **Type**: String
- **Description**: The name of the race track or venue where the race is taking place
- **Example**: "Nswhrc at Tabcorp Pk Menangle", "Albion Park", "Cranbourne"

### RaceNumber
- **Type**: Integer
- **Description**: The sequential number of the race on the race day
- **Example**: 1, 2, 3, 4, etc.

### RaceName
- **Type**: String
- **Description**: The official name or title of the specific race
- **Example**: "MENANGLE COUNTRY CLUB TROTTERS MOBILE", "APG 2YO C & G BULLION HEAT"

### RaceDistance
- **Type**: Integer
- **Description**: The distance of the race in meters
- **Example**: 1609, 1660, 1740, 2080, 2190, 2300

### RaceTitle
- **Type**: String
- **Description**: Additional race information including prize money and conditions
- **Example**: "$9,180 NR up to 70. PBD/NR. Mobile"

## Horse Identification

### HorseNumber
- **Type**: Integer
- **Description**: The horse's number in the specific race (starting gate position)
- **Range**: 1-12+

### HorseName
- **Type**: String
- **Description**: The official registered name of the horse
- **Example**: "VALLEY ESS JAY", "KYLIES LIFE", "VICTREE HILL"

### HorseID
- **Type**: Integer
- **Description**: Unique identifier for the horse in the database
- **Example**: 777582, 797122, 805682

### Form
- **Type**: String/Number
- **Description**: Recent racing form showing finishing positions in recent races
- **Example**: "11484", "86165", "60210"

## Race Participants

### Trainer
- **Type**: String
- **Description**: Name of the horse's trainer
- **Example**: "David McElhinney", "Joseph Pace", "Courtney Slater"

### Driver
- **Type**: String
- **Description**: Name of the driver/jockey for this race, with claim allowances if applicable
- **Example**: "Bryse McElhinney (C,5)", "Jim Douglass", "Michael Stanley"

### Handicap
- **Type**: Integer
- **Description**: Handicap weight or advantage assigned to the horse
- **Example**: 0 (most common), indicating no handicap

## Horse Demographics

### DayCalender
- **Type**: Date
- **Description**: The date of the race
- **Format**: YYYY-MM-DD
- **Example**: "2021-04-13"

### age
- **Type**: Integer
- **Description**: Age of the horse in years
- **Range**: 2-10+
- **Example**: 2, 4, 6, 9

### sex
- **Type**: String
- **Description**: Gender of the horse
- **Values**: 
  - GELDING (castrated male)
  - MARE (female)
  - HORSE (intact male)
  - COLT (young male)
  - FILLY (young female)

### sire
- **Type**: String
- **Description**: The name of the horse's father (sire)
- **Example**: "SKYVALLEY NZ", "LIFE SIGN USA", "TRIXTON (US)"

## Performance Statistics

### LifetimeRuns
- **Type**: Integer
- **Description**: Total number of races the horse has participated in during its career
- **Example**: 110, 63, 11

### LifetimeWins
- **Type**: Integer
- **Description**: Total number of races won in the horse's career
- **Example**: 15, 6, 3

### LifetimeSeconds
- **Type**: Integer
- **Description**: Total number of second-place finishes in career
- **Example**: 16, 3, 3

### LifetimeThirds
- **Type**: Integer
- **Description**: Total number of third-place finishes in career
- **Example**: 8, 4, 0

### LifetimePlacings
- **Type**: Integer
- **Description**: Total number of top-three finishes (win/place/show)
- **Example**: 39, 13, 6

### LifetimeWinPercent
- **Type**: Float (0-1)
- **Description**: Percentage of races won over the horse's career
- **Calculation**: LifetimeWins / LifetimeRuns
- **Example**: 0.136 (13.6%), 0.095 (9.5%)

### LifetimePlacePercent
- **Type**: Float (0-1)
- **Description**: Percentage of races finished in top three over career
- **Calculation**: LifetimePlacings / LifetimeRuns
- **Example**: 0.355 (35.5%), 0.206 (20.6%)

## Recent Performance

### RecentRuns
- **Type**: Integer
- **Description**: Number of races in recent period (typically last 5-10 races)
- **Example**: 7, 14, 0

### RecentWins
- **Type**: Integer
- **Description**: Number of wins in recent races
- **Example**: 2, 2, 0

### RecentSeconds
- **Type**: Integer
- **Description**: Number of second-place finishes in recent races
- **Example**: 1, 0, 0

### RecentThirds
- **Type**: Integer
- **Description**: Number of third-place finishes in recent races
- **Example**: 0, 1, 0

### RecentPlacings
- **Type**: Integer
- **Description**: Total top-three finishes in recent races
- **Example**: 3, 3, 0

### RecentWinPercent
- **Type**: Float (0-1)
- **Description**: Win percentage in recent races
- **Example**: 0.286 (28.6%), 0.143 (14.3%)

### RecentPlacePercent
- **Type**: Float (0-1)
- **Description**: Place percentage (top 3) in recent races
- **Example**: 0.429 (42.9%), 0.214 (21.4%)

## Race Conditions

### Row
- **Type**: Integer
- **Description**: Starting position row (front row = 1, second row = 2, etc.)
- **Example**: 1, 2, 3, 4, 5

### Class
- **Type**: Integer
- **Description**: Class rating or grade of the horse
- **Example**: 57, 59, 59, 60, 62

### Dayssincelast
- **Type**: Integer
- **Description**: Number of days since the horse's last race
- **Example**: 7, 14, 119, 24

### firstup
- **Type**: Integer (0/1)
- **Description**: Whether this is the horse's first race after a break
- **Values**: 0 = No, 1 = Yes

### spelllastfive
- **Type**: Integer
- **Description**: Information about breaks in the last five races
- **Example**: 0

### Firststarter
- **Type**: Integer (0/1)
- **Description**: Whether this is the horse's first ever race
- **Values**: 0 = No, 1 = Yes

## Betting Information

### StartingOdds
- **Type**: Float
- **Description**: The betting odds for the horse at race start
- **Example**: 41, 51, 15, 3.25

### laststart
- **Type**: Integer
- **Description**: Finishing position in the horse's last race
- **Example**: 4, 5, 0, 2

### start2, start3, start4
- **Type**: Integer
- **Description**: Finishing positions in the 2nd, 3rd, and 4th most recent races
- **Example**: 8, 6, 1 (for start2, start3, start4 respectively)

## Track and Performance Metrics

### Gatespeedstrikerate
- **Type**: Float (0-1)
- **Description**: Success rate at achieving good gate speed (quick start)
- **Example**: 0.264, 0.222, 0.091

### broken
- **Type**: Float
- **Description**: Rate of breaking gait (losing proper gait during race)
- **Example**: 0.055, 0.016, 0.091

### LeaderStrikeRate
- **Type**: Float (0-1)
- **Description**: Rate of leading or being in front during races
- **Example**: 0.218, 0.159, 0.273

## Additional Features

### GearChanges
- **Type**: Integer
- **Description**: Number of gear/equipment changes made for this race
- **Example**: 1, 6, 0, 4

### GearRemoved
- **Type**: String/NULL
- **Description**: Equipment removed for this race
- **Most values**: NULL (no gear removed)

### trials
- **Type**: Integer
- **Description**: Number of trial races the horse has participated in
- **Note**: Many values are NULL

### Winner
- **Type**: Integer (0/1)
- **Description**: Target variable - whether the horse won this race
- **Values**: 0 = Did not win, 1 = Won the race
- **Note**: This is the prediction target for machine learning models

## Data Quality Notes

1. **NULL Values**: Many fields contain NULL values, particularly in the latter columns, indicating optional or unavailable information.

2. **Calculated Fields**: Several percentage fields are calculated from base statistics (e.g., win percentages from wins/runs).

3. **Time-Dependent**: Recent performance metrics are time-dependent and reflect the horse's form at the time of the race.

4. **Race-Specific**: Some fields (like Row, Driver, Trainer) are specific to the individual race rather than inherent horse characteristics.

## Usage for Machine Learning

This dataset is well-suited for predicting race outcomes, with:
- **Target Variable**: `Winner` (binary classification)
- **Features**: All other fields can serve as predictive features
- **Key Predictors**: Recent performance metrics, odds, class ratings, and track conditions typically show strong predictive power
- **Feature Engineering**: Consider creating additional features like form trends, trainer/driver success rates, and track-specific performance metrics

The rich feature set allows for comprehensive analysis of factors affecting horse racing outcomes, making it valuable for both predictive modeling and racing analytics.
