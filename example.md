### Example
* Consider reworking check-conflict w.r.t. concrete programs. Currently, if a concrete program passes the spec verification on the first IO example in the list, then it is concretely checked against the rest. This leaves out possible learning opportunities for the other examples, so it would be better to do learning on the other examples first before verifying the program. It may end up that doing the latter is slower (as perhaps concrete programs that satisfy the spec for one IO example heuristically tend to satisfy the rest).

* Rethink the backtracking method - it seems like a huge bottleneck to be storing every single visited (incorrect) partial program in a list. The original intention was to only store concrete programs.
  - Maybe somehow optionally keep track of the current hole and its attempted productions?

* Iteratively deepen the search depth to try the shortest programs first. This is more of a heuristic that assumes most target programs will be short (will on average increase runtime for longer programs), but will have the bonus of finding the shortest programs possible.

* Support list output. Not sure if this is feasible given how we deal with lists symbolically. If it is, it'll take a lot of casing.

[Lorem ipsum](/lorem.md) is a great test tool.