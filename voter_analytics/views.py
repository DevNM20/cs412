#File: views.py
# Author: Nathan Moges (bmoges18@bu.edu) 10/3/2025
# Description: This file views.py has two different views for the single voter view and the list of voters
# which are the ListView and DetaileView


from django.views.generic import ListView, DetailView
from .models import Voter

class VoterListView(ListView):
    '''View to display and filter voter records of the city of Newton'''
    model = Voter
    template_name = 'voter_analytics/voter_list.html'
    context_object_name = 'voters'
    paginate_by = 100

    def get_queryset(self):
        '''Filter the voter queryset based on GET parameters'''
        voters = super().get_queryset()

        # Retrieve filters from query parameters
        party = self.request.GET.get('party')
        min_dob = self.request.GET.get('min_dob')
        max_dob = self.request.GET.get('max_dob')
        voter_score = self.request.GET.get('voter_score')

        # Apply filters if present
        if party:
            voters = voters.filter(party_affilitation__iexact=party)

        if min_dob:
            voters = voters.filter(dob__gte=min_dob)

        if max_dob:
            voters = voters.filter(dob__lte=max_dob)

        if voter_score:
            voters = voters.filter(voter_score=voter_score)

        for election in ['v20state', 'v21town', 'v21primary', 'v22general', 'v23town']:
            if self.request.GET.get(election):
                voters = voters.filter(**{election: True})

        return voters 

class VoterDetailView(DetailView):
    """View to display a single voter's complete record"""
    model = Voter
    template_name = "voter_analytics/voter_detail.html"
    context_object_name = "voter"
