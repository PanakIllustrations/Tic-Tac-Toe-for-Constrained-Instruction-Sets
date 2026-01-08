# Tic-Tac-Toe-for-Constrained-Instruction-Sets
A tic-tac-toe implementation designed to run within the limitations of G-Code on CNC machines (specifically Haas controllers).


### The Challenge

Haas CNC machines store all values as floats internally and don't support native binary operations. Most efficient tic-tac-toe implementations use bitboards—compact binary representations where each bit represents a board square. Bitboards typically rely on operations like AND, OR, and bit shifts that aren't available in G-Code.

### The Solution

This implementation recreates bitboard functionality using only floating-point arithmetic:
| Standard Operation | Float-Based Implementation | 
| ------- | -------- |
| Set bit | bb + 2^i | 
| Get bit | floor(bb / 2^i) % 2 | 
| Bitwise AND | Loop through bits, compare, sum matching positions | 

Win detection uses bitmasks for all 8 winning lines (3 rows, 3 columns, 2 diagonals) and checks if a player's bitboard contains all bits in any mask.

### AI Difficulty

The AI uses the same logic at all difficulty levels—it always blocks losing moves and takes winning moves. Difficulty is controlled entirely by move priority order when no immediate win/block exists:
| Difficulty | Priority |
| ---------- | -------- |
| Easy | OrderEasyEdges → Corners → Center |
| Medium | Corners → Center → Edges |
| Impossible | Center → Corners → Edges |

This creates natural-feeling difficulty without randomness.

#### Files

TicTacToeDemo.py — Python proof-of-concept using only G-Code-compatible operations

#### Status

Proof of concept. Not yet translated to G-Code.
