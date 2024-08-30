class CreatePluReglements < ActiveRecord::Migration[7.0]
    def change
        create_table :plu_reglements do |t|
            t.column :idterritoire, :string,  limit: 10, null: false
            t.column :codcom,       :string,  limit: 6,  null: false
            t.column :annee,        :integer,            null: false
            t.column :zone,         :string,  limit: 2,  null: false
            t.column :section,      :string,  limit: 10, null: false
            t.column :hauteur,      :decimal, precision: 5, scale: 2
            t.column :emprise,      :decimal, precision: 5, scale: 2

            t.index :%i[idterritoire zone section], unique: true

            t.timestamps
        end
    end
end
