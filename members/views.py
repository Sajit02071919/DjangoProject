from django.views.generic import ListView
from django.views.generic.dates import timezone_today

from members.models import CorporateMember, DeveloperMember


class DeveloperMemberListView(ListView):
    model = DeveloperMember
    context_object_name = 'members'

    def get_queryset(self):
        return super().get_queryset().filter(member_until=None)

    def get_context_data(self):
        context = super().get_context_data()
        context['former_members'] = DeveloperMember.objects.filter(
            member_until__lte=timezone_today(),
        )
        return context


class CorporateMemberListView(ListView):
    model = CorporateMember
    context_object_name = 'members'

    def get_queryset(self):
        return self.model.objects.for_public_display()