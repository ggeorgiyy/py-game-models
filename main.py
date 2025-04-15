import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    pass


if __name__ == "__main__":
    main()
    obj, created = Race.objects.get_or_create(
        name="Humans",
        description ="Very nice and smart creatures"
    )

    obj, created = Skill.objects.get_or_create(
        name="Tutor",
        bonus ="Can train other creatures"
    )

    obj, created = Guild.objects.get_or_create(
        name="Rebellion_1",
        description ="Fight against the Empire"
    )

    Players = {}
    try:
        obj = Player.objects.get(nickname="10", email="10@gmai.com")
        for key, value in Players.items():
            setattr(obj, key, value)
        obj.save()
    except Player.DoesNotExist:
        new_values = {"nickname": "10", "email": "10@gmai.com"}
        new_values.update(Players)
        obj = Player(**new_values)
        obj.save()

