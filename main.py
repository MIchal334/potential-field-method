
import field_generator
import move

if __name__ == "__main__":
  field_generator.generate_field()
  move_gen = move.move_generator()
  move_gen.move()