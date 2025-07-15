# Gear Changes Dataset Documentation

## Overview
This dataset contains comprehensive information about horse racing events with a focus on gear changes and detailed race statistics. Each row represents a horse in a specific race with their performance metrics, gear modifications, and historical data.

## Dataset Details
- **File**: `gear_changes.csv`
- **Total Records**: 13,282 entries
- **Primary Focus**: Gear changes and their impact on horse performance

## Field Descriptions

### Race Information
| Field | Type | Description |
|-------|------|-------------|
| `Venue` | String | Racing venue/track name (e.g., "Nswhrc at Tabcorp Pk Menangle") |
| `RaceNumber` | Integer | Sequential race number at the venue |
| `RaceName` | String | Official name of the race |
| `RaceDistance` | Integer | Race distance in meters |
| `RaceTitle` | String | Race title with prize money and conditions |
| `DayCalender` | Date | Date of the race (YYYY-MM-DD format) |

### Horse Basic Information
| Field | Type | Description |
|-------|------|-------------|
| `HorseNumber` | Integer | Horse's number in the race |
| `HorseName` | String | Official name of the horse |
| `HorseID` | Integer | Unique identifier for the horse |
| `Horsename50` | String | Truncated horse name (50 characters) |
| `age` | Integer | Age of the horse in years |
| `sex` | String | Gender of the horse (GELDING, MARE, HORSE) |
| `sire` | String | Name of the horse's father/sire |

### Race Setup & Position
| Field | Type | Description |
|-------|------|-------------|
| `Row` | Integer | Starting position row (1=front row, 2=second row, etc.) |
| `Handicap` | Integer | Handicap distance in meters |
| `Form` | String | Recent form guide showing recent race results |
| `Trainer` | String | Name of the horse's trainer |
| `Driver` | String | Name of the driver/jockey |
| `StartingOdds` | Float | Betting odds at race start |

### Performance History
| Field | Type | Description |
|-------|------|-------------|
| `LifetimeRuns` | Integer | Total number of races the horse has participated in |
| `LifetimeWins` | Integer | Total career wins |
| `LifetimeSeconds` | Integer | Total career second-place finishes |
| `LifetimeThirds` | Integer | Total career third-place finishes |
| `LifetimePlacings` | Integer | Total career top-3 finishes |
| `LifetimeWinPercent` | Float | Career win percentage (0-1 scale) |
| `LifetimePlacePercent` | Float | Career placing percentage (0-1 scale) |

### Recent Performance (Last 5-7 races)
| Field | Type | Description |
|-------|------|-------------|
| `RecentRuns` | Integer | Number of recent races |
| `RecentWins` | Integer | Recent wins |
| `RecentSeconds` | Integer | Recent second-place finishes |
| `RecentThirds` | Integer | Recent third-place finishes |
| `RecentPlacings` | Integer | Recent top-3 finishes |
| `RecentWinPercent` | Float | Recent win percentage |
| `RecentPlacePercent` | Float | Recent placing percentage |

### Racing Behavior & Statistics
| Field | Type | Description |
|-------|------|-------------|
| `Gatespeedstrikerate` | Float | Success rate when achieving gate speed |
| `broken` | Float | Frequency of breaking gait/stride |
| `LeaderStrikeRate` | Float | Success rate when leading the race |
| `Class` | Integer | Racing class/grade level |
| `Dayssincelast` | Integer | Days since last race |
| `firstup` | Boolean | First race after a spell (0/1) |
| `spelllastfive` | Boolean | Had a spell in last 5 starts |
| `Firststarter` | Boolean | First career race (0/1) |

### Last Start Information
| Field | Type | Description |
|-------|------|-------------|
| `laststart` | Integer | Result of last start |
| `start2` | Integer | Result of second last start |
| `start3` | Integer | Result of third last start |
| `start4` | Integer | Result of fourth last start |
| `TrackLastStart` | String | Track where last race was run |
| `RowLastStart` | Integer | Starting row in last race |
| `DistanceLastStart` | Integer | Distance of last race |
| `TrainerLastStart` | String | Trainer in last race |
| `DriverLastStart` | String | Driver in last race |

### Gear Changes (Primary Focus)
| Field | Type | Description |
|-------|------|-------------|
| `GearChanges` | String | Details of gear added for this race |
| `GearRemoved` | String | Details of gear removed for this race |

### Performance Metrics
| Field | Type | Description |
|-------|------|-------------|
| `BestWinningMile` | String | Best winning mile rate time |
| `samedistance` | Boolean | Racing at same distance as last start |
| `UpInDistance` | Boolean | Racing at longer distance than last start |
| `DownInDistance` | Boolean | Racing at shorter distance than last start |
| `TimesLead` | Integer | Number of times horse has led races |
| `TimesGateSpeed` | Integer | Number of times achieved gate speed |
| `TimesBroken` | Integer | Number of times broken gait |

### Financial Information
| Field | Type | Description |
|-------|------|-------------|
| `PrizemoneyLastStart` | Float | Prize money earned in last start |
| `Prizemoney` | Float | Total prize money for this race |
| `Prizemoneylastrace` | Float | Prize money from last race |
| `avestake` | Float | Average stake/bet amount |
| `totalprize` | Float | Total prize pool |
| `prizemoneyup` | Boolean | Prize money higher than last race |
| `prizemoneydown` | Boolean | Prize money lower than last race |
| `prizemoneysame` | Boolean | Prize money same as last race |

### Track & Conditions
| Field | Type | Description |
|-------|------|-------------|
| `sametrack` | Boolean | Racing at same track as last start |
| `tracknamelaststart` | String | Name of track where last race was run |
| `morningrace` | Boolean | Morning race time |
| `eveningrace` | Boolean | Evening race time |
| `morningracelaststart` | Boolean | Last race was in morning |
| `eveningracelaststart` | Boolean | Last race was in evening |

### Race Timing
| Field | Type | Description |
|-------|------|-------------|
| `racetime` | String | Official race time |
| `Timelastrace` | String | Time of last race |
| `Triallaststart` | Boolean | Last start was a trial |
| `Standlaststart` | Boolean | Last start was standing start |

### Professional Changes
| Field | Type | Description |
|-------|------|-------------|
| `NumberTrainer` | Integer | Trainer identifier number |
| `driverchange` | Boolean | Driver changed from last start |
| `trainerchange` | Boolean | Trainer changed from last start |
| `trials` | Integer | Number of trial races |

### Position Analysis
| Field | Type | Description |
|-------|------|-------------|
| `aveplace` | Float | Average finishing position |
| `countofdeath` | Integer | Count of death seat positions (outside front row) |
| `Deathseat` | Boolean | Starting from death seat position |
| `Leading` | Boolean | Currently leading or likely to lead |
| `frontrow` | Boolean | Starting from front row |
| `secondrow` | Boolean | Starting from second row |

### Detailed Position Counts
| Field | Type | Description |
|-------|------|-------------|
| `countfront1` | Integer | Count of races from position 1 |
| `countfront2` | Integer | Count of races from position 2 |
| `countfront3` | Integer | Count of races from position 3 |
| `countfront4` | Integer | Count of races from position 4 |
| `countld1` | Integer | Count of leading from position 1 |
| `countld2` | Integer | Count of leading from position 2 |
| `countld3` | Integer | Count of leading from position 3 |
| `countld4` | Integer | Count of leading from position 4 |

### Betting Information
| Field | Type | Description |
|-------|------|-------------|
| `startingprice1` | Float | Starting price/odds |
| `StewardsFull` | String | Full stewards' comments |

## Key Features for Analysis

### 1. Gear Change Impact
- `GearChanges` and `GearRemoved` are the primary fields for analyzing gear modifications
- These can be correlated with performance improvements or declines

### 2. Performance Predictors
- `RecentWinPercent` and `LifetimeWinPercent` for win probability
- `Gatespeedstrikerate` and `LeaderStrikeRate` for tactical analysis
- `broken` rate for reliability assessment

### 3. Class and Competition Level
- `Class` indicates the competition level
- `StartingOdds` reflects market confidence
- Prize money fields indicate race quality

### 4. Track and Distance Factors
- `samedistance`, `UpInDistance`, `DownInDistance` for distance suitability
- `sametrack` for track familiarity
- `Dayssincelast` for freshness/fitness

## Data Quality Notes
- Many fields contain NULL values, especially in the latter columns
- Percentages are stored as decimals (0-1 scale)
- Boolean fields use 0/1 encoding
- Some fields may require cleaning for analysis

## Usage Recommendations
This dataset is ideal for:
- Predicting race outcomes based on gear changes
- Analyzing the effectiveness of different equipment modifications
- Building machine learning models for horse racing predictions
- Studying the relationship between gear changes and performance improvements
