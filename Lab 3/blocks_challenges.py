import student_block as sb
import pet_block as pb

def start_student_block():
    name = sb.start_program()
    age, status = sb.acquaint(name)
    sb.get_organization_information(status=status)

    scores = sb.get_scores(name, status)
    sb.say_scores_count(sb.get_scores_count(*scores))

def start_pet_block():
    pet = pb.start_block(pb.create_pet, pb.say_pet_properties)
    pb.get_voice(pet)
    pb.update_pet(pet, pb.say_pet_properties)