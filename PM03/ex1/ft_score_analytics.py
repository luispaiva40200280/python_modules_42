from sys import argv as argv


def score_statistics(scores: list[int]) -> None:
    print("=== Player Score Analytics ===")
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


def ft_score_analytics(argv: list[str]) -> None:
    list_score: list[str] | None = argv[1:]
    if not list_score:
        print("No scores provided. "
              + "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    scores: list[int] | None = []
    for score in list_score:
        try:
            s: int | ValueError = int(score)
            scores.append(s)
        except ValueError:
            print("oops, I typed ’banana’ instead of ’1000’")

    if not scores:
        print("Error: no valid scores")
        return
    if len(scores) == 1:
        print(f"Only one valid score: {scores[0]}")
    else:
        score_statistics(scores)


if __name__ == "__main__":
    ft_score_analytics(argv)
