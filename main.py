
import field_generator
import move
import filed_data

if __name__ == "__main__":
  filed_data.create_positive_shape()
  field_generator.generate_field()
  move_gen = move.move_generator()
  move_gen.move()