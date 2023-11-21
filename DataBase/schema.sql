CREATE TABLE cricket_match_data_live (
    unique_id INT PRIMARY KEY AUTO_INCREMENT,
    match_id INT,
    inning INT,
    batting_team VARCHAR(255),
    bowling_team VARCHAR(255),
    `over` INT,
    ball INT,
    batsman VARCHAR(255),
    non_striker VARCHAR(255),
    bowler VARCHAR(255),
    is_super_over INT,
    wide_runs INT,
    bye_runs INT,
    legbye_runs INT,
    noball_runs INT,
    penalty_runs INT,
    batsman_runs INT,
    extra_runs INT,
    total_runs INT,
    player_dismissed VARCHAR(255),
    dismissal_kind VARCHAR(255),
    fielder VARCHAR(255)
);
