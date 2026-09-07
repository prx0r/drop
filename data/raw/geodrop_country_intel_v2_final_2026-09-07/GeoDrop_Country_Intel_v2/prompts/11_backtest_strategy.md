# Strategy Backtest Agent
Use TRUE_HISTORICAL only when every required evidence item has available_at <= as_of. Otherwise use RECONSTRUCTED_HISTORICAL and downgrade confidence. Freeze strategy version and full candidate universe. Evaluate precision@k, false positives/reasons, time/capital to validation, realized contribution and calibration. Prefer prospective shadow tests.
