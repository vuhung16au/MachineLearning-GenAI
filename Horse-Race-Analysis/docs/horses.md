# Horses Dataset Documentation

## Overview

This dataset contains comprehensive horse racing data across multiple files (`horses.csv`, `horses1.csv`, `horses2.csv`) with detailed race results, horse performance metrics, and racing conditions. Each record represents a horse's participation in a specific race with complete performance history and race context.

## Dataset Details

- **Files**: `horses.csv`, `horses1.csv`, `horses2.csv`
- **Primary Focus**: Horse performance analysis and race outcome prediction
- **Note**: horses1.csv includes an additional `id` field, while horses2.csv has extended fields for detailed analysis

## Field Descriptions

### Race Identification

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Unique record identifier (horses1.csv only) |
| `RaceNumber` | Integer | Sequential race number at the venue |
| `RaceName` | String | Official name of the race event |
| `RaceTitle` | String | Detailed race title with conditions and prize money |
| `RaceDistance` | Integer | Race distance in meters |
| `Venue` | String | Racing venue/track name |
| `DayCalender` | Date | Date of the race (YYYY-MM-DD format) |

### Race Results & Performance

| Field | Type | Description |
|-------|------|-------------|
| `Place` | Integer | Final finishing position in the race |
| `Winner` | Boolean | Whether the horse won the race (1=Yes, 0=No) |
| `Prizemoney` | Float | Prize money earned in this race |
| `Margin` | Float | Winning/losing margin (lengths behind winner) |
| `MarginWinner` | Float | Margin by which the winner won |
| `StartingOdds` | Float | Betting odds at race start |
| `BSP` | Float | Betfair Starting Price (horses2.csv) |

### Horse Information

| Field | Type | Description |
|-------|------|-------------|
| `HorseName` | String | Official name of the horse |
| `Horsename50` | String | Truncated horse name (50 characters) |
| `HorseID` | Integer | Unique identifier for the horse |
| `Age` | Integer | Age of the horse in years |
| `Sex` | String | Gender of the horse (GELDING, MARE, HORSE, etc.) |
| `Colour` | String | Color description of the horse |
| `Sire` | String | Name of the horse's father/sire |

### Race Setup & Conditions

| Field | Type | Description |
|-------|------|-------------|
| `Row` | Integer | Starting position row (1=front, 2=second, etc.) |
| `Handicap` | Integer | Handicap distance in meters |
| `Trainer` | String | Name of the horse's trainer |
| `Driver` | String | Name of the driver/jockey |
| `Placer` | String | Placing information |
| `TrackRating` | Float | Official track rating/condition |
| `weather` | String | Weather conditions (horses2.csv) |
| `trackCondition` | String | Track surface condition (horses2.csv) |

### Race Times & Sectionals

| Field | Type | Description |
|-------|------|-------------|
| `Gross_Time` | String | Total race time |
| `Mile_Rate` | Float | Mile rate (time per mile) |
| `Lead_Time` | Float | Time spent in the lead |
| `First_Quarter` | Float | First quarter sectional time |
| `Second_Quarter` | Float | Second quarter sectional time |
| `Third_Quarter` | Float | Third quarter sectional time |
| `Fourth_Quarter` | Float | Fourth quarter sectional time |

### Career Statistics

| Field | Type | Description |
|-------|------|-------------|
| `Firststarter` | Boolean | First career race (0/1) |
| `LifetimeRuns` | Integer | Total career race starts |
| `LifetimeWins` | Integer | Total career wins |
| `LifetimeSeconds` | Integer | Total career second-place finishes |
| `LifetimeThirds` | Integer | Total career third-place finishes |
| `LifetimePlacings` | Integer | Total career top-3 finishes |
| `LifetimeWinPercent` | Float | Career win percentage (0-1 scale) |
| `LifetimePlacePercent` | Float | Career placing percentage (0-1 scale) |

### Recent Form (Last 5-7 races)

| Field | Type | Description |
|-------|------|-------------|
| `RecentRuns` | Integer | Number of recent races |
| `RecentWins` | Integer | Recent wins |
| `RecentSeconds` | Integer | Recent second-place finishes |
| `RecentThirds` | Integer | Recent third-place finishes |
| `RecentPlacings` | Integer | Recent top-3 finishes |
| `RecentWinPercent` | Float | Recent win percentage |
| `RecentPlacePercent` | Float | Recent placing percentage |

### Racing Behavior & Tactics

| Field | Type | Description |
|-------|------|-------------|
| `Class` | Integer | Racing class/grade level |
| `Dayssincelast` | Integer | Days since last race start |
| `Gatespeedstrikerate` | Float | Success rate when achieving gate speed |
| `broken` | Float | Frequency of breaking gait/stride |
| `LeaderStrikeRate` | Float | Success rate when leading |
| `Leading` | Boolean | Led at some point in the race |
| `Deathseat` | Boolean | Started from disadvantageous outside front position |

### Recent Starts History

| Field | Type | Description |
|-------|------|-------------|
| `laststart` | Integer | Result of most recent start |
| `start2` | Integer | Result of second most recent start |
| `start3` | Integer | Result of third most recent start |
| `start4` | Integer | Result of fourth most recent start |

### Distance Analysis

| Field | Type | Description |
|-------|------|-------------|
| `SameDistance` | Boolean | Racing at same distance as last start |
| `FiftyPercentile` | Float | Performance percentile at this distance |
| `BestMileRateint` | Integer | Best mile rate as integer |
| `firsttimeatdistance` | Boolean | First time racing at this distance |
| `upindistance` | Boolean | Racing at longer distance than usual |
| `downindistance` | Boolean | Racing at shorter distance than usual |
| `mostrunsatdistance` | Integer | Most runs at this specific distance |

### Position During Race

| Field | Type | Description |
|-------|------|-------------|
| `OneBehind` | Boolean | Positioned one behind the leader |
| `OneOne` | Boolean | In the "one-one" position (second, outside leader) |
| `FifthPegs` | Boolean | Racing in fifth position or back |
| `Worsethanfifth` | Boolean | Positioned worse than fifth |

### Professional Connections

| Field | Type | Description |
|-------|------|-------------|
| `Trainerruns` | Integer | Number of horses this trainer has run |
| `Trainerstrikerate` | Float | Trainer's success rate |
| `Driverruns` | Integer | Number of drives by this driver |
| `Driverstrikerate` | Float | Driver's success rate |
| `driverchange` | Boolean | Driver changed from last start |
| `trainerchange` | Boolean | Trainer changed from last start |
| `trackchange` | Boolean | Different track from last start |

### Draw & Starting Position Analysis

| Field | Type | Description |
|-------|------|-------------|
| `NumberofHorses` | Integer | Total number of horses in the race |
| `Racesfromsecondrow` | Integer | Number of races started from second row |
| `Racesfromfrontrow` | Integer | Number of races started from front row |
| `GSfromdrawonetwo` | Integer | Gate speed achieved from barrier 1-2 |
| `GSfromdrawthreefour` | Integer | Gate speed achieved from barrier 3-4 |
| `GSfromdrawrestoffront` | Integer | Gate speed achieved from other front row positions |
| `GSandleadwhengsinside` | Integer | Gate speed and lead from inside draws |
| `GSandleadwhengsoutside` | Integer | Gate speed and lead from outside draws |

### Financial & Prize Information

| Field | Type | Description |
|-------|------|-------------|
| `aveprizemoney` | Float | Average prize money earned |
| `countgatespeedonfrontrow` | Integer | Count of gate speed from front row |
| `homevenue` | Boolean | Racing at home/preferred venue |

### Extended Fields (horses2.csv only)

| Field | Type | Description |
|-------|------|-------------|
| `RowLastStart` | Integer | Starting row in last race |
| `DistanceLastStart` | Integer | Distance of last race |
| `TrainerLastStart` | String | Trainer in last race |
| `DriverLastStart` | String | Driver in last race |
| `StewardsFull` | String | Complete stewards' comments |
| `BestWinningMile` | Float | Best winning mile rate |
| `TimeLead` | Integer | Times led during races |
| `TimeGateSpeed` | Integer | Times achieved gate speed |
| `TimeBroken` | Integer | Times broken gait |
| `PrizemoneyLastStart` | Float | Prize money from last start |
| `Triallaststart` | Boolean | Last start was a trial |
| `Standlaststart` | Boolean | Last start was standing start |
| `racetime` | String | Race start time |
| `morningrace` | Boolean | Morning race time |
| `eveningrace` | Boolean | Evening race time |
| `Timelastrace` | String | Time of last race |
| `morningracelaststart` | Boolean | Last race was in morning |
| `eveningracelaststart` | Boolean | Last race was in evening |
| `Prizemoneylastrace` | Float | Prize money from last race |
| `startingprice1` | Float | Alternative starting price |
| `avestake` | Float | Average stake amount |
| `totalprize` | Float | Total prize pool |
| `sametrack` | Boolean | Same track as last start |
| `prizemoneysame` | Boolean | Same prize money as last race |
| `prizemoneyup` | Boolean | Higher prize money than last race |
| `prizemoneydown` | Boolean | Lower prize money than last race |
| `Tracklaststart` | String | Track code for last start |
| `tracknamelaststart` | String | Track name for last start |
| `trials` | Integer | Number of trial races |
| `aveplace` | Float | Average finishing position |
| `countld1` through `countld4` | Integer | Count of leads from different positions |
| `countfront1` through `countfront4` | Integer | Count of starts from front positions |
| `countofdeath` | Integer | Count of death seat starts |
| `frontrow` | Boolean | Starting from front row |
| `secondrow` | Boolean | Starting from second row |
| `NumberTrainer` | Integer | Trainer identifier number |

### Race Start Types

| Field | Type | Description |
|-------|------|-------------|
| `bestwinningmileratelastwin` | Float | Best mile rate in last winning performance |
| `standingstartlaststart` | Boolean | Last start was standing start |
| `insiderunningline` | Boolean | Raced on inside of track |
| `outsiderunningline` | Boolean | Raced on outside of track |
| `mobilestart` | Boolean | Mobile start type |

### Stewards & Comments

| Field | Type | Description |
|-------|------|-------------|
| `StewardsComments` | String | Official stewards' report |
| `Scratching` | String | Scratching information if applicable |

## Key Features for Machine Learning

### Target Variables
- `Winner`: Primary target for win/loss prediction
- `Place`: For finish position prediction
- `Prizemoney`: For earnings prediction

### Important Predictors
- `RecentWinPercent` & `LifetimeWinPercent`: Historical performance
- `StartingOdds`: Market confidence indicator
- `Class`: Competition level
- `Dayssincelast`: Freshness factor
- `Row`: Starting advantage
- `SameDistance`: Distance suitability

### Feature Engineering Opportunities
- Form trends from `laststart`, `start2`, `start3`, `start4`
- Professional success rates from trainer/driver statistics
- Track and distance familiarity indicators
- Recent vs. lifetime performance comparisons

## Data Quality Notes
- Large file sizes may require memory management
- Some fields contain NULL/missing values
- Boolean fields use 1/0 encoding
- Percentages stored as decimals (0-1 scale)
- Time fields may need parsing for analysis

## Usage Recommendations

This dataset is excellent for:
- **Win Prediction Models**: Using performance history and race conditions
- **Odds Analysis**: Comparing market odds with actual outcomes
- **Performance Trends**: Analyzing career trajectories and form cycles
- **Track & Distance Optimization**: Understanding horse preferences
- **Professional Analysis**: Evaluating trainer and driver effectiveness

The rich feature set makes this ideal for machine learning approaches including logistic regression, neural networks, and ensemble methods for horse racing prediction models.
