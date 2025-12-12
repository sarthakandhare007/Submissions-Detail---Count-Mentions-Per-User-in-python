import heapq

class Solution:
    def countMentions(self, numberOfUsers, events):
        mentions = [0] * numberOfUsers
        online = [True] * numberOfUsers
        heap = []  # (come_online_time, user_id)

        processed = []
        for e in events:
            processed.append((e[0], int(e[1]), e[2]))

        # OFFLINE must come before MESSAGE when timestamps are equal
        priority = {"OFFLINE": 0, "MESSAGE": 1}
        processed.sort(key=lambda x: (x[1], priority[x[0]]))

        for event_type, timestamp, data in processed:

            # Restore users whose offline timeout ends before current event
            while heap and heap[0][0] <= timestamp:
                _, uid = heapq.heappop(heap)
                online[uid] = True

            if event_type == "OFFLINE":
                uid = int(data)
                online[uid] = False
                heapq.heappush(heap, (timestamp + 60, uid))

            else:  # MESSAGE
                msg = data
                if msg == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1

                elif msg == "HERE":
                    for i in range(numberOfUsers):
                        if online[i]:
                            mentions[i] += 1

                else:
                    ids = msg.split()
                    for token in ids:
                        uid = int(token[2:])
                        mentions[uid] += 1

        return mentions
