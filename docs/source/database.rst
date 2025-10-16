###################################
Modèles de la Base de Données
###################################

Cette section décrit les modèles de données utilisés dans l'application.

-----------------------------------

.. _lettings_models:

Application "Lettings"
======================

.. autoclass:: lettings.models.Address
   :members: __str__

   .. attribute:: number
      :type: PositiveIntegerField

      Le numéro de la rue.

   .. attribute:: street
      :type: CharField(max_length=64)

      Le nom de la rue.

   .. attribute:: city
      :type: CharField(max_length=64)

      La ville.

   .. attribute:: state
      :type: CharField(max_length=2)

      L'État (code à 2 lettres).

   .. attribute:: zip_code
      :type: PositiveIntegerField

      Le code postal.

   .. attribute:: country_iso_code
      :type: CharField(max_length=3)

      Le code ISO du pays (3 lettres).


.. autoclass:: lettings.models.Letting
   :members: __str__

   .. attribute:: title
      :type: CharField(max_length=256)

      Le titre de l'annonce de location.

   .. attribute:: address
      :type: OneToOneField(to=Address)

      L'adresse associée à cette location. Relation un-à-un.


-----------------------------------

.. _profiles_models:

Application "Profiles"
======================


.. autoclass:: profiles.models.Profile
   :members: __str__

   .. attribute:: user
      :type: OneToOneField(to=User)

      L'utilisateur Django associé à ce profil. Relation un-à-un.

   .. attribute:: favorite_city
      :type: CharField(max_length=64)

      La ville favorite de l'utilisateur.