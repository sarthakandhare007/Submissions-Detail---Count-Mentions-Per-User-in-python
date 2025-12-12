# Submissions-Detail---Count-Mentions-Per-User-in-python
Maintain an array online = [True] * numberOfUsers

Maintain mentions = [0] * numberOfUsers

Maintain a priority queue (min-heap) for automatic online events:
→ (timeUserComesOnline, userId)

Process events in chronological order:

Before processing each event:

Bring back any users whose “come online time” has passed

If event is "OFFLINE":

Set online[id] = False

Add (timestamp + 60, id) to heap

If event is "MESSAGE":

If mentions_string is:

"ALL" → mention every user

"HERE" → mention online users only

"idX idY..." → extract IDs, count occurrences even if offline
