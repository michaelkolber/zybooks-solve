import errors  # Import this first to avoid circular import issues
import solver

s = solver.zyBooksSession(credentials_path='credentials.json')
s.solve_all()
