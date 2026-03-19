with open("code.txt", "r") as f:
    code = f.read()

loops = code.lower().count("for") + code.lower().count("while")

if loops == 0:
    complexity = "O(1)"
elif loops == 1:
    complexity = "O(n)"
elif loops == 2:
    complexity = "O(n^2)"
else:
    complexity = "O(n^" + str(loops) + ")"

print("\n========== CODE REVIEW REPORT ==========")
print(f"Loops Found: {loops}")
print(f"Estimated Complexity: {complexity}")

if loops >= 2:
    print("\n⚠ Issues:")
    print("- Nested loops detected (high complexity)")

    print("\n💡 Suggestions:")
    print("- Try optimizing using better data structures (e.g., HashMap)")
else:
    print("\n✅ Code looks efficient")

if "def" in code:
    print("\n⚠ Recursion detected (check stack usage)")

if code.count("\n") > 20:
    print("\n⚠ Code is too long, consider breaking into smaller functions")