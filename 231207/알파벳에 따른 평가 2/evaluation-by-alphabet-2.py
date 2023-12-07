c = input()

ans = {
    'S': 'Superior',
    'F': 'Fantastic',
    'G': 'Good',
    'U': 'Usually',
    'E': 'Effort',
}

print(ans[c] if c in ['S', 'F', 'G', 'U', 'E'] else 'Failure')