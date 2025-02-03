from models import Notes

print('--- All Notes ---')
notes = Notes.objects()
for note in notes:
    records = [f'description: {record.description}, done: {record.done}' for record in note.records]
    tags = [tag.name for tag in note.tags]
    print(f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}")

print('--- Notes with tag Fun ---')

notes = Notes.objects(tags__name='Fun')
for note in notes:
    records = [f'description: {record.description}, done: {record.done}' for record in note.records]
    tags = [tag.name for tag in note.tags]
    print(f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}")


# Example of update:
# _id = '6318789480a92d0f3a49c7cb'
# note = Notes.objects(id=_id)
# note.update(name='New name')

# Example of deletion :
# _id = '6318789480a92d0f3a49c7cb'
# note = Notes.objects(id=_id).delete()