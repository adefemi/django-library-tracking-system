from celery import shared_task
from django.utils import timezone
from library.models import Loan

@shared_task
def check_overdue_loans():
    member_with_due_loans = Loan.objects.filter(
        is_returned=False, due_date__lt=timezone.now()).select_related("member", "member__user")

    for member in member_with_due_loans:
        # send mail to members
        print(f"Sending reminder to member with email: {member.user.email}")
        pass