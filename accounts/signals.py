from django.db.models.signals import post_migrate, post_save
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from .models import PawMedicUser
from .choices import PawMedicUserType


@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    if sender.name == "accounts":
        vet_permissions = [
            # Vet profile management
            "accounts.change_vetprofile",
            "accounts.view_vetprofile",
            # Appointment scheduling
            "appointments.change_appointmentslot",
            "appointments.view_appointmentslot",
            "appointments.view_appointment",
            # Forum - full CRUD
            "forum.add_forumpost",
            "forum.change_forumpost",
            "forum.delete_forumpost",
            "forum.view_forumpost",
            "forum.add_comment",
            "forum.change_comment",
            "forum.delete_comment",
            "forum.view_comment",
            # Tag management (as per README - vets manage tags)
            "forum.add_tag",
            "forum.change_tag",
            "forum.delete_tag",
            "forum.view_tag",
            # View pets (as per README)
            "pets.view_pet",
        ]

        owner_permissions = [
            # Appointment booking
            "appointments.add_appointment",
            "appointments.view_appointment",
            # Forum - full CRUD
            "forum.add_forumpost",
            "forum.change_forumpost",
            "forum.delete_forumpost",
            "forum.view_forumpost",
            "forum.add_comment",
            "forum.change_comment",
            "forum.delete_comment",
            "forum.view_comment",
            # Pet management - full CRUD
            "pets.add_pet",
            "pets.change_pet",
            "pets.delete_pet",
            "pets.view_pet",
        ]

        # Create or update Vets group
        vets_group, _ = Group.objects.get_or_create(name="Vets")
        vets_group.permissions.clear()
        for perm_codename in vet_permissions:
            app_label, codename = perm_codename.split(".")
            try:
                perm = Permission.objects.get(
                    content_type__app_label=app_label, codename=codename
                )
                vets_group.permissions.add(perm)
            except Permission.DoesNotExist:
                print(f"Warning: Permission {perm_codename} not found")

        # Create or update Pet Owners group
        owners_group, _ = Group.objects.get_or_create(name="Pet Owners")
        owners_group.permissions.clear()
        for perm_codename in owner_permissions:
            app_label, codename = perm_codename.split(".")
            try:
                perm = Permission.objects.get(
                    content_type__app_label=app_label, codename=codename
                )
                owners_group.permissions.add(perm)
            except Permission.DoesNotExist:
                print(f"Warning: Permission {perm_codename} not found")

        print("User groups 'Vets' and 'Pet Owners' created with permissions.")


@receiver(post_save, sender=PawMedicUser)
def assign_user_to_group(sender, instance, created, **kwargs):
    if created:
        if instance.role == PawMedicUserType.VET:
            vets_group = Group.objects.get(name="Vets")
            instance.groups.add(vets_group)
            print(f"Assigned user {instance.username} to 'Vets' group")
        elif instance.role == PawMedicUserType.OWNER:
            owners_group = Group.objects.get(name="Pet Owners")
            instance.groups.add(owners_group)
            print(f"Assigned user {instance.username} to 'Pet Owners' group")
