import { Component, OnInit } from '@angular/core';
import { Bens } from '../../shared/bens.model';
import { BensService } from '../../shared/services/bens.service';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.scss']
})
export class IndexComponent implements OnInit {

  bens: Bens[] = [];

  constructor(private bensService: BensService) { }

  ngOnInit(): void {
    this.bensService.getAll().subscribe( b => this.bens = b);
  }

}
