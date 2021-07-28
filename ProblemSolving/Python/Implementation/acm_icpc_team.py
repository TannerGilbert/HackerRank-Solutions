import os


def acmTeam(topic):
    max_num_topics = 0
    num_teams = 0
    for t in topic:
        for t2 in topic:
            t_combined = int(t, 2) | int(t2, 2)
            num_topics = list(f"{t_combined:b}").count("1")
            if num_topics > max_num_topics:
                max_num_topics = num_topics
                num_teams = 1
            elif num_topics == max_num_topics:
                num_teams += 1
    return (max_num_topics, num_teams // 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
